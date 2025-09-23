// @ts-check
const { test as base } = require('@playwright/test');

// Create a test fixture that handles authentication
const test = base.extend({
  // This fixture provides an authenticated page
  authenticatedPage: async ({ page }, use) => {
    // Navigate to the verification page
    await page.goto('/verify');
    
    // Fill in the verification form
    await page.fill('input[name="answer"]', 'test verification');
    await page.click('button[type="submit"]');
    
    // Wait for navigation to complete
    await page.waitForURL('**/');
    
    // Use the authenticated page in the test
    await use(page);
  },
});

module.exports = { test };
