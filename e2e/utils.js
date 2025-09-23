// Helper function to bypass verification
async function bypassVerification(page, baseURL) {
  console.log('Bypassing verification...');
  const bypassUrl = new URL('/bypass-verification', baseURL).toString();
  await page.goto(bypassUrl, { waitUntil: 'networkidle' });

  // Verify we're on the home page
  const searchInput = await page.$('input[type="text"]');
  if (!searchInput) {
    throw new Error('Failed to bypass verification - search input not found');
  }
  console.log('Successfully bypassed verification');
}

module.exports = {
  bypassVerification
};