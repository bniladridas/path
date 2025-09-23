// @ts-check
const { defineConfig, devices } = require('@playwright/test');

/**
 * @see https://playwright.dev/docs/test-configuration
 */
module.exports = defineConfig({
  testDir: './e2e',
  // Global timeout for all tests (30 minutes)
  timeout: 30 * 60 * 1000,
  
  expect: {
    // Maximum time expect() should wait for the condition to be met (10 seconds)
    timeout: 10000,
    
    // Add custom matchers for better test assertions
    toMatchSnapshot: { maxDiffPixelRatio: 0.01 },
  },
  
  // Run tests in files in parallel
  fullyParallel: false,
  
  // Fail the build on CI if you accidentally left test.only in the source code.
  forbidOnly: !!process.env.CI,
  
  // Retry failed tests on CI with 2 retries
  retries: process.env.CI ? 2 : 1,
  
  // Limit the number of workers for stability
  workers: 1,
  
  // Reporter to use
  reporter: [
    ['list'],
    ['html', { 
      open: 'never',
      outputFolder: 'playwright-report',
      outputName: 'index.html'
    }],
    ['github'],
    ['json', { outputFile: 'test-results/results.json' }]
  ],
  
  // Shared settings for all the projects
  use: {
    // Base URL to use in actions like `await page.goto('/')`
    baseURL: process.env.BASE_URL || 'http://localhost:8000',
    
    // Maximum time each action such as `click()` can take (30 seconds)
    actionTimeout: 30000,
    
    // Maximum time navigation operations can take (30 seconds)
    navigationTimeout: 30000,
    
    // Collect trace when retrying the failed test
    trace: 'on-first-retry',
    
    // Capture screenshot after each test failure
    screenshot: 'only-on-failure',
    
    // Record video for each test
    video: 'on-first-retry',
    
    // Viewport settings
    viewport: { width: 1280, height: 720 },
    
    // Ignore HTTPS errors
    ignoreHTTPSErrors: true,
    
    // Bypass CSP for testing
    bypassCSP: true,
    
    // Headless mode in CI, headed locally
    headless: !!process.env.CI,
    
    // Browser language
    locale: 'en-US',
    
    // Timezone
    timezoneId: 'UTC',
    
    // Geolocation
    geolocation: { longitude: 12.492507, latitude: 41.889938 },
    
    // Permissions
    permissions: ['geolocation'],
    
    // Emulate network conditions
    offline: false,
  },
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        viewport: { width: 1280, height: 800 },
        launchOptions: {
          devtools: !process.env.CI,
          args: [
            '--disable-dev-shm-usage', // Overcome limited resource problems
            '--disable-web-security', // Disable same-origin policy
            '--disable-features=IsolateOrigins,site-per-process', // Disable site isolation
            '--no-sandbox', // Disable sandbox mode
            '--disable-setuid-sandbox', // Disable setuid sandbox
            '--disable-gpu', // Disable GPU hardware acceleration
            '--disable-software-rasterizer', // Disable software rasterizer
            '--disable-dev-shm-usage', // Overcome limited resource problems
            '--disable-features=RendererCodeIntegrity', // Disable renderer code integrity
            '--disable-blink-features=AutomationControlled', // Disable automation controlled flag
          ],
        },
        contextOptions: {
          ignoreHTTPSErrors: true,
          acceptDownloads: true,
          bypassCSP: true,
          offline: false,
          geolocation: { longitude: 12.492507, latitude: 41.889938 },
          permissions: ['geolocation', 'notifications'],
          timezoneId: 'UTC',
          locale: 'en-US',
          colorScheme: 'light',
          viewport: { width: 1280, height: 800 },
          deviceScaleFactor: 1,
          isMobile: false
        },
      },
    },
    // Uncomment to test in other browsers
    /*
    {
      name: 'firefox',
      use: { 
        ...devices['Desktop Firefox'],
        viewport: { width: 1280, height: 800 },
      },
    },
    {
      name: 'webkit',
      use: { 
        ...devices['Desktop Safari'],
        viewport: { width: 1280, height: 800 },
      },
    },
    */
  ],
  outputDir: 'test-results/',
});
