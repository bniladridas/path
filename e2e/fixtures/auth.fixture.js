// @ts-check
const { test: base } = require('@playwright/test');

const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    await page.goto('/verify');
    await page.fill('input[name="answer"]', 'human');
    await page.click('button[type="submit"]');
    await page.waitForURL(new RegExp(`${page.url().replace(/\/verify$/, '')}/$`));
    await use(page);
  },
});

module.exports = { test, expect: require('@playwright/test').expect };
