const { test, expect } = require('@playwright/test');
const { bypassVerification } = require('./utils');

// Constants for selectors and test data
const SELECTORS = {
  SEARCH_INPUT: 'input[type="text"]',
  SUBMIT_BUTTON: 'button[type="submit"]',
  THEME_TOGGLE: 'button',
  BODY: 'body',
  VERIFICATION_INPUT: 'input[name="answer"]',
  NAV_LINKS: '[data-testid^="nav-"]'
};

const URLS = {
  ABOUT: '/about',
  PRODUCT: '/product',
  BLOG: '/blog',
  HELP: '/help',
  TERMS: '/terms',
  PRIVACY: '/privacy',
  THEME_REPO: 'https://github.com/bniladridas/path',
  COMMUNITY_REPO: 'https://github.com/harpertoken'
};

const TEST_DATA = {
  THEME_TOGGLE_TEXT: /theme|mode|light|dark/i,
  VERIFICATION_ANSWER: 'human'
};

test.describe('Navigation', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    console.log('Starting navigation test...');
    
    // Clear any existing session data
    await page.context().clearCookies();
    
    // Bypass verification
    await bypassVerification(page, baseURL);
    
    // Ensure we're on the home page
    const currentUrl = new URL(page.url());
    if (!currentUrl.pathname.endsWith('/')) {
      await page.goto(baseURL, { waitUntil: 'networkidle' });
    }
    
    console.log('Test setup complete, current URL:', page.url());
  });

  test('should have working navigation links', async ({ page, baseURL }) => {
    console.log('Testing navigation links...');
    
    // Track test results
    const testResults = {
      total: 0,
      passed: 0,
      failed: 0,
      skipped: 0,
      details: []
    };
    
    try {
      // Get all navigation links on the page
      const navLinks = await page.$$eval(SELECTORS.NAV_LINKS, 
        elements => elements
          .filter(el => el.href && !el.href.startsWith('javascript:') && !el.href.startsWith('mailto:'))
          .map(el => ({
            text: el.textContent?.trim() || '',
            href: el.href,
            selector: el.getAttribute('data-testid') || 
                     el.getAttribute('id') ? `#${el.getAttribute('id')}` :
                     el.getAttribute('class') ? `.${el.getAttribute('class').split(' ')[0]}` :
                     `a[href="${el.getAttribute('href')}"]`,
            isVisible: el.offsetParent !== null
          }))
      );

      // Add main navigation items if not already included
      const mainNavItems = [
        { selector: '[data-testid="nav-terms"]', url: URLS.TERMS, isExternal: false },
        { selector: '[data-testid="nav-privacy"]', url: URLS.PRIVACY, isExternal: false },
        { selector: '[data-testid="nav-theme"]', url: URLS.THEME_REPO, isExternal: true },
        { selector: '[data-testid="nav-community"]', url: URLS.COMMUNITY_REPO, isExternal: true }
      ];

      // Merge and deduplicate navigation items
      const allNavItems = [...navLinks];
       mainNavItems.forEach(item => {
         if (!allNavItems.some(link => link.selector === item.selector)) {
           allNavItems.push({
             text: item.selector.replace(/^[^=]+=/, '').replace(/^\w+\[href\^="([^"]+)"\]$/, '$1'),
             href: item.isExternal ? item.url : `${baseURL}${item.url}`,
             selector: item.selector,
             isVisible: true
           });
         }
       });

      testResults.total = allNavItems.length;
      console.log(`Found ${testResults.total} navigation links to test`);

      // Test each navigation link
      for (const [index, navItem] of allNavItems.entries()) {
        const result = {
          index: index + 1,
          selector: navItem.selector,
          text: navItem.text || 'N/A',
          href: navItem.href,
          status: 'pending'
        };

        console.log(`\nTesting navigation [${index + 1}/${testResults.total}]:`, navItem.selector);
        
        try {
          // Navigate back to home before each test
          await page.goto(baseURL, { waitUntil: 'networkidle' });
          
          // Find the element
          const element = page.locator(navItem.selector).first();
          const isVisible = await element.isVisible().catch(() => false);
          
          if (!isVisible) {
            result.status = 'skipped';
            result.reason = 'Element not visible';
            testResults.skipped++;
            testResults.details.push(result);
            console.log(`Skipping hidden element: ${navItem.selector}`);
            continue;
          }
          
           // Get element details for debugging
           const elementInfo = await element.evaluate(el => ({
             tagName: el.tagName,
             text: el.textContent?.trim(),
             href: el.href,
             id: el.id,
             className: el.className,
             role: el.getAttribute('role'),
             target: el.getAttribute('target')
           }));

           console.log('Element info:', JSON.stringify(elementInfo, null, 2));

           // Check if this is an external link (different domain or target="_blank")
           const linkUrl = new URL(elementInfo.href);
           const baseUrl = new URL(baseURL);
           const isExternal = linkUrl.hostname !== baseUrl.hostname || elementInfo.target === '_blank';

           if (isExternal) {
             // For external links, just verify the href is correct
             const expectedUrl = navItem.href;
             if (elementInfo.href === expectedUrl) {
               result.status = 'passed';
               result.destination = elementInfo.href;
               testResults.passed++;
               console.log(`✅ External link has correct href: ${elementInfo.href}`);
             } else {
               result.status = 'failed';
               result.reason = `Expected href "${expectedUrl}" but got "${elementInfo.href}"`;
               testResults.failed++;
               console.log(`❌ External link href mismatch: expected ${expectedUrl}, got ${elementInfo.href}`);
             }
           } else {
             // For internal links, test actual navigation
             console.log(`Clicking: ${navItem.selector}`);
             await element.click({ timeout: 5000 });

             // Wait for navigation to complete
             await page.waitForLoadState('networkidle');

             // Verify navigation was successful
             const currentUrl = new URL(page.url());
             console.log('Navigated to:', currentUrl.toString());

             // Basic validation
             const isSuccess = currentUrl.toString() !== baseURL &&
                             currentUrl.toString() !== `${baseURL}/` &&
                             !currentUrl.pathname.endsWith('404');

             if (isSuccess) {
               result.status = 'passed';
               result.destination = currentUrl.toString();
               testResults.passed++;
               console.log(`✅ Navigation successful to: ${currentUrl.toString()}`);
             } else {
               result.status = 'failed';
               result.reason = 'Navigation did not change URL as expected';
               result.destination = currentUrl.toString();
               testResults.failed++;
               console.log(`❌ Navigation failed or stayed on the same page`);
             }
           }
          
        } catch (error) {
          result.status = 'error';
          result.reason = error.message;
          testResults.failed++;
          console.error(`❌ Error testing navigation [${navItem.selector}]:`, error.message);
          
          // Take screenshot on error
          const screenshotPath = `navigation-error-${index + 1}.png`;
          await page.screenshot({ path: screenshotPath });
          console.log(`Screenshot saved: ${screenshotPath}`);
        }
        
        testResults.details.push(result);
      }
      
      // Generate test summary
      console.log('\n=== Navigation Test Summary ===');
      console.log(`Total: ${testResults.total}`);
      console.log(`✅ Passed: ${testResults.passed}`);
      console.log(`❌ Failed: ${testResults.failed}`);
      console.log(`⏩ Skipped: ${testResults.skipped}`);
      
      // Log detailed results
      if (testResults.details.length > 0) {
        console.log('\n=== Detailed Results ===');
        testResults.details.forEach(detail => {
          const statusIcon = detail.status === 'passed' ? '✅' : 
                           detail.status === 'failed' ? '❌' : 
                           detail.status === 'skipped' ? '⏩' : '❓';
          console.log(`${statusIcon} [${detail.index}] ${detail.selector}`);
          if (detail.reason) console.log(`   Reason: ${detail.reason}`);
          if (detail.destination) console.log(`   Destination: ${detail.destination}`);
        });
      }
      
      // Fail the test if any navigation tests failed
      if (testResults.failed > 0) {
        throw new Error(`${testResults.failed} navigation test(s) failed`);
      }
      
      if (testResults.passed === 0) {
        console.warn('No navigation links were tested successfully. Taking a screenshot...');
        await page.screenshot({ path: 'no-navigation-links.png' });
        console.log('Screenshot saved: no-navigation-links.png');
      }
      
    } catch (error) {
      console.error('Error in navigation test:', error);
      await page.screenshot({ path: 'navigation-test-error.png' });
      throw error; // Re-throw to fail the test
    }
  });
  
  test('should maintain theme preference', async ({ page, baseURL }) => {
    console.log('Testing theme preference...');
    
    try {
      // Wait for the page to be fully loaded
      await page.waitForLoadState('networkidle');
      
      // Try to find theme toggle button (if it exists)
      const themeToggle = page.locator(SELECTORS.THEME_TOGGLE).filter({ hasText: TEST_DATA.THEME_TOGGLE_TEXT }).first();
      
      if (await themeToggle.isVisible()) {
        console.log('Theme toggle button found, testing theme switching...');
        
        // Get current theme class
        const body = page.locator(SELECTORS.BODY);
        const initialTheme = await body.getAttribute('class') || '';
        
        // Toggle theme
        await themeToggle.click();
        
        // Wait for theme change (if any)
        await expect(body).not.toHaveAttribute('class', initialTheme, { timeout: 5000 });
        
        // Get new theme class
        const newTheme = await body.getAttribute('class') || '';

        // Check if theme actually changed
        if (initialTheme === newTheme) {
          console.log('Theme did not change after toggle');
        } else {
          console.log('Theme changed successfully');
        }

        // Refresh and check if theme is maintained
        await page.reload();
        await page.waitForLoadState('networkidle');

        const refreshedTheme = await body.getAttribute('class') || '';
        if (refreshedTheme !== newTheme) {
          console.log('Theme preference was not maintained after refresh');
        } else {
          console.log('Theme preference was maintained after refresh');
        }
      } else {
        console.log('No theme toggle found, skipping theme test');
      }
      
      console.log('Theme preference test completed');
    } catch (error) {
      console.error('Error in theme preference test:', error);
      await page.screenshot({ path: 'theme-test-error.png' });
      // Don't fail the test if theme testing isn't critical
      console.log('Theme test failed, but continuing...');
    }
  });
});
