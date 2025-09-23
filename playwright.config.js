// @ts-check
const { defineConfig, devices } = require('@playwright/test');

/**
 * @see https://playwright.dev/docs/test-configuration
 */
module.exports = defineConfig({
  testDir: './e2e',
  timeout: 120 * 1000, // Increase timeout to 2 minutes
  expect: {
    timeout: 10000, // Increase expect timeout to 10 seconds
  },
  fullyParallel: false, // Run tests in serial to avoid port conflicts
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 1, // Retry failed tests once in local development
  workers: 1, // Run tests one at a time
  reporter: [
    ['list'],
    ['html', { open: 'never' }],
  ],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:8000',
    actionTimeout: 10000, // Increase action timeout to 10 seconds
    navigationTimeout: 30000, // Increase navigation timeout to 30 seconds
    trace: 'on-first-retry',
    screenshot: 'only-on-failure', // Take screenshots only on failure
    video: 'retain-on-failure', // Record video only on failure
  },
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        viewport: { width: 1280, height: 720 },
      },
    },
    // Disable other browsers for now to speed up testing
    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },
    // {
    //   name: 'webkit',
    //   use: { ...devices['Desktop Safari'] },
    // },
  ],
  // Server is started by the GitHub Actions workflow
  // to better handle port conflicts
});
