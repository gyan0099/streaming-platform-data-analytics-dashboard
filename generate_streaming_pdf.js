const puppeteer = require('/Users/vedprakash/Desktop/Dav project/node_modules/puppeteer');
const fs = require('fs');
const path = require('path');

const BASE_DIR = '/Users/vedprakash/Desktop/Dav project';
const HTML_FILE = path.join(BASE_DIR, 'presentation_deck.html');

const OUTPUT_PDFS = [
    path.join(BASE_DIR, 'Streaming_Platforms_Dashboard_Presentation.pdf'),
    path.join(BASE_DIR, 'GYAN_DAV_LAB_PROJECT_1.pdf'),
    '/Users/vedprakash/Desktop/Streaming_Platforms_Dashboard_Presentation.pdf',
    '/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1.pdf',
    '/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1/Streaming_Platforms_Dashboard_Presentation.pdf',
    '/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1/GYAN_DAV_LAB_PROJECT_1.pdf'
];

(async () => {
    try {
        const chromePath = process.env.PUPPETEER_EXECUTABLE_PATH ||
            (fs.existsSync('/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell')
                ? '/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell'
                : (fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
                    ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                    : undefined));

        console.log('Launching browser with Chrome at:', chromePath);
        const browser = await puppeteer.launch({
            headless: 'new',
            executablePath: chromePath,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });

        const page = await browser.newPage();
        await page.setViewport({ width: 1920, height: 1080 });
        
        console.log('Navigating to local HTML deck...');
        await page.goto(`file://${HTML_FILE}`, { waitUntil: 'networkidle0', timeout: 60000 });

        console.log('Generating 10-slide PDF for Streaming Platforms Dashboard...');
        const primaryPdf = OUTPUT_PDFS[0];
        await page.pdf({
            path: primaryPdf,
            width: '1920px',
            height: '1080px',
            printBackground: true,
            margin: { top: 0, right: 0, bottom: 0, left: 0 }
        });

        console.log(`Successfully generated primary PDF: ${primaryPdf} (${fs.statSync(primaryPdf).size} bytes)`);

        for (let i = 1; i < OUTPUT_PDFS.length; i++) {
            const dest = OUTPUT_PDFS[i];
            fs.mkdirSync(path.dirname(dest), { recursive: true });
            fs.copyFileSync(primaryPdf, dest);
            console.log(`Copied to: ${dest}`);
        }

        await browser.close();
        console.log('All PDF deliverables successfully produced for Streaming Platforms Dashboard!');
        process.exit(0);
    } catch (err) {
        console.error('Error generating PDF:', err);
        process.exit(1);
    }
})();
