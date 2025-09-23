const { test, expect } = require('@playwright/test');

test.describe('Verification Flow', () => {
  test('should redirect to verification page when not verified', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveURL(/\/verify$/);
  });

  test('should show error for incorrect verification', async ({ page }) => {
    await page.goto('/verify');
    
    // Submit empty form
    await page.click('button[type="submit"]');
    
    // Check for error message
    const errorMessage = page.locator('.error-message');
    await expect(errorMessage).toBeVisible();
    await expect(errorMessage).toContainText('verification failed');
  });

  test('should redirect to home after successful verification', async ({ page }) => {
    await page.goto('/verify');
    
    // Fill in the verification form
    await page.fill('input[name="answer"]', 'test verification');
    await page.click('button[type="submit"]');
    
    // Should be redirected to home page
    await expect(page).toHaveURL('/');
    
    // Verify session is maintained
    await page.reload();
    await expect(page).toHaveURL('/');
  });
});
