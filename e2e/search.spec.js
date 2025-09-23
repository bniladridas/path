const { test, expect } = require('./fixtures/auth.fixture');

test.describe('Search Functionality', () => {
  test('should display search input on home page', async ({ authenticatedPage: page }) => {
    await expect(page.locator('input[type="text"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
  });

  test('should show loading state during search', async ({ authenticatedPage: page }) => {
    // Mock the API response
    await page.route('**/search', route => {
      // Simulate network delay
      setTimeout(() => {
        route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({ response: 'Test response' })
        });
      }, 1000);
    });

    // Perform search
    await page.fill('input[type="text"]', 'test search');
    await page.click('button[type="submit"]');
    
    // Check loading state
    await expect(page.locator('.loading-indicator')).toBeVisible();
    
    // Wait for response and check results
    await expect(page.locator('.response-container')).toBeVisible();
  });

  test('should display search results', async ({ authenticatedPage: page }) => {
    // Mock the API response
    await page.route('**/search', route => {
      route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ response: 'Test response' })
      });
    });

    // Perform search
    await page.fill('input[type="text"]', 'test search');
    await page.click('button[type="submit"]');
    
    // Check results
    await expect(page.locator('.response-container')).toContainText('test response');
  });

  test('should handle search errors gracefully', async ({ authenticatedPage: page }) => {
    // Mock error response
    await page.route('**/search', route => {
      route.fulfill({
        status: 500,
        contentType: 'application/json',
        body: JSON.stringify({ error: 'Internal server error' })
      });
    });

    // Perform search
    await page.fill('input[type="text"]', 'error test');
    await page.click('button[type="submit"]');
    
    // Check error message
    await expect(page.locator('.error-message')).toBeVisible();
    await expect(page.locator('.error-message')).toContainText('error');
  });
});
