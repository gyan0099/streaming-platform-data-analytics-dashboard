const puppeteer = require('puppeteer');
(async () => {
        const fs = require('fs');
    const chromePath = process.env.PUPPETEER_EXECUTABLE_PATH ||
        (fs.existsSync('/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell')
            ? '/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell'
            : (fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
                ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                : undefined));
    const browser = await puppeteer.launch({
        headless: "new",
        executablePath: chromePath,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    page.on('console', msg => console.log('LOG:', msg.text()));
    page.on('requestfailed', request => {
      console.log(`Failed request: ${request.url()} - ${request.failure().errorText}`);
    });
    page.on('response', response => {
      if (!response.ok()) {
        console.log(`Error response: ${response.url()} - ${response.status()}`);
      }
    });
    await page.setViewport({width: 1200, height: 800});
    await page.goto('http://localhost:8000/dashboard.html', {waitUntil: 'domcontentloaded'});
    await page.screenshot({path: 'screenshot.png'});
    await browser.close();
})();
