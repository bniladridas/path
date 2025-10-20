const { test, expect } = require('@playwright/test');

// Set a longer timeout for all tests
test.setTimeout(120000);

test.describe('Verification Flow', () => {
  test('should redirect to verification page when not verified', async ({ page, baseURL }) => {
    console.log('Base URL from config:', baseURL);
    console.log('Navigating to home page...');

    try {
      await page.goto(baseURL, {
        waitUntil: 'domcontentloaded',
        timeout: 30000
      });
      console.log('Current URL after navigation:', page.url());

      // Take a screenshot for debugging
      await page.screenshot({ path: 'homepage-navigation.png' });

      // Check if we're on the verification page
      const currentUrl = page.url();
      if (!currentUrl.includes('/verify')) {
        console.log('Unexpected page content:', await page.content());
      }

      await expect(page).toHaveURL(/\/verify$/);
    } catch (error) {
      console.error('Navigation error:', error);
      // Take a screenshot on error
      await page.screenshot({ path: 'navigation-error.png' });
      throw error;
    }
  });

  test('should show error for incorrect verification', async ({ page, baseURL }) => {
    console.log('Navigating to verification page...');
    const verifyUrl = new URL('/verify', baseURL).toString();
    console.log('Verify URL:', verifyUrl);

    try {
      await page.goto(verifyUrl, {
        waitUntil: 'domcontentloaded',
        timeout: 30000
      });

      console.log('Page URL:', page.url());
      await page.screenshot({ path: 'before-submit.png' });

      console.log('Submitting empty form...');
      await page.click('button[type="submit"]');

      console.log('Waiting for error message...');
      // Wait for the error message to appear
      await expect(page.locator('body')).toContainText('please try again', { timeout: 5000 });

      await page.screenshot({ path: 'after-submit.png' });

       // Check page content for error message
       const pageContent = (await page.content()).toLowerCase();
       console.log('Page content length:', pageContent.length);

       // The actual error message is 'please try again'
       expect(pageContent).toContain('please try again');
    } catch (error) {
      console.error('Test error:', error);
      await page.screenshot({ path: 'test-error.png' });
      throw error;
    }
  });

  test('should use bypass verification for testing', async ({ page, baseURL }) => {
    console.log('Using bypass verification for testing...');

    // Navigate to the bypass endpoint
    const bypassUrl = new URL('/bypass-verification', baseURL).toString();
    await page.goto(bypassUrl, { waitUntil: 'networkidle' });

    console.log('After bypass, current URL:', page.url());

    // Verify we're on the home page by checking for the search input
    const searchInput = await page.$('input[type="text"]');
    if (!searchInput) {
      console.log('Search input not found after bypass. Current page content:');
      console.log(await page.content());
      throw new Error('Failed to bypass verification - search input not found');
    }

    console.log('Successfully bypassed verification');
  });

  test('should redirect to home after successful verification', async ({ page, baseURL }) => {
    console.log('Testing verification flow...');

    // First clear any existing verification
    await page.context().clearCookies();
    await page.context().clearPermissions();

    // Navigate to the verification page
    const verifyUrl = new URL('/verify', baseURL).toString();
    await page.goto(verifyUrl, { waitUntil: 'networkidle' });
    console.log('On verification page:', page.url());

    // Check if we're on the verification page
    const currentUrl = new URL(page.url());
    if (!currentUrl.pathname.endsWith('/verify')) {
      console.log('Unexpected redirect during verification test. Current URL:', page.url());
      await page.screenshot({ path: 'verification-unexpected-redirect.png' });
      throw new Error('Unexpected redirect during verification test');
    }

    // Fill in the verification form with a valid answer
    console.log('Filling verification form...');
    await page.fill('input[name="answer"]', 'human');

    // Submit the form
    console.log('Submitting verification form...');
    await Promise.all([
      page.waitForNavigation({ waitUntil: 'networkidle' }),
      page.click('button[type="submit"]')
    ]);

    console.log('After verification, current URL:', page.url());

    // Check if we're on the home page
    const finalUrl = new URL(page.url());
    if (!finalUrl.pathname.endsWith('/')) {
      console.log('Verification failed - not redirected to home page');
      console.log('Current page content:', await page.content());
      await page.screenshot({ path: 'verification-failed.png' });
      throw new Error('Verification failed - not redirected to home page');
    }

    // Verify search input is visible
    const searchInput = await page.$('input[type="text"]');
    if (!searchInput) {
      console.log('Search input not found after verification');
      throw new Error('Search input not found after verification');
    }

    console.log('Verification test completed successfully');
  });
});
