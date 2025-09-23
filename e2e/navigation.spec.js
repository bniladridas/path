const { test, expect } = require('./fixtures/auth.fixture');

test.describe('Navigation', () => {
  test('should navigate to terms page', async ({ authenticatedPage: page }) => {
    await page.click('text=Terms of Use');
    await expect(page).toHaveURL(/\/terms$/);
    await expect(page.locator('h1')).toContainText('Terms of Use');
  });

  test('should navigate to privacy page', async ({ authenticatedPage: page }) => {
    await page.click('text=Privacy Policy');
    await expect(page).toHaveURL(/\/privacy$/);
    await expect(page.locator('h1')).toContainText('Privacy Policy');
  });

  test('should navigate to updates page', async ({ authenticatedPage: page }) => {
    await page.click('text=Updates');
    await expect(page).toHaveURL(/\/updates$/);
    await expect(page.locator('h1')).toContainText('Latest Updates');
  });

  test('should maintain theme preference', async ({ authenticatedPage: page }) => {
    // Change theme
    await page.click('button[aria-label="Change theme"]');
    await page.click('text=Dark');
    
    // Check if theme is applied
    const body = page.locator('body');
    await expect(body).toHaveClass(/dark-theme/);
    
    // Refresh and check if theme is maintained
    await page.reload();
    await expect(body).toHaveClass(/dark-theme/);
  });
});
