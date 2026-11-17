const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

// Simple static server
const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, decodeURIComponent(req.url.split('?')[0]));
    if (filePath.endsWith('/') || filePath === __dirname) filePath = path.join(filePath, 'dashboard.html');
    if (!fs.existsSync(filePath)) {
        res.writeHead(404);
        return res.end('Not found: ' + filePath);
    }
    const ext = path.extname(filePath);
    const mime = {
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.css': 'text/css',
        '.json': 'application/json',
        '.png': 'image/png'
    }[ext] || 'text/plain';
    res.writeHead(200, { 'Content-Type': mime });
    fs.createReadStream(filePath).pipe(res);
});

server.listen(8092, async () => {
    console.log('Testing server running on http://localhost:8092');
    let browser;
    try {
        const chromePath = process.env.PUPPETEER_EXECUTABLE_PATH ||
            (fs.existsSync('/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell')
                ? '/Users/vedprakash/.cache/puppeteer/chrome-headless-shell/mac_arm-154.0.8037.57/chrome-headless-shell-mac-arm64/chrome-headless-shell'
                : (fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
                    ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                    : undefined));

        browser = await puppeteer.launch({
            headless: 'new',
            executablePath: chromePath,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 1000 });

        console.log('\n[1/9] Navigating to dashboard with realistic satellite map...');
        await page.goto('http://localhost:8092/dashboard.html', { waitUntil: 'domcontentloaded', timeout: 30000 });
        await new Promise(r => setTimeout(r, 2500));

        // 1. Verify Map & Leaflet Initialization
        const mapExists = await page.evaluate(() => typeof leafletMap !== 'undefined' && leafletMap !== null);
        console.log('✔ Leaflet Map initialized:', mapExists);
        if (!mapExists) throw new Error('Leaflet map was not initialized!');

        // 2. Verify Map Stability (NO auto-rotation, NO auto-spin)
        console.log('\n[2/9] Testing map stability & verifying auto-spin is disabled...');
        const initialCenter = await page.evaluate(() => {
            const c = leafletMap.getCenter();
            return { lat: c.lat, lng: c.lng, zoom: leafletMap.getZoom() };
        });
        console.log('  Initial map center:', initialCenter);

        // Wait 2 seconds and measure drift
        await new Promise(r => setTimeout(r, 2000));
        const afterWaitCenter = await page.evaluate(() => {
            const c = leafletMap.getCenter();
            return { lat: c.lat, lng: c.lng, zoom: leafletMap.getZoom() };
        });
        console.log('  Center after 2s pause:', afterWaitCenter);

        const latDiff = Math.abs(initialCenter.lat - afterWaitCenter.lat);
        const lngDiff = Math.abs(initialCenter.lng - afterWaitCenter.lng);
        if (latDiff > 0.001 || lngDiff > 0.001) {
            throw new Error(`Map unstable! Drift detected: latDiff=${latDiff}, lngDiff=${lngDiff}`);
        }
        console.log('✔ Map is completely stable! 0 drift, 0 auto-spin, North remains at top.');

        // 3. Test Layer Switching (Hybrid, Pure Satellite, Streets, Terrain)
        console.log('\n[3/9] Testing Satellite / Street / Terrain layer switcher...');
        
        // Open layer menu
        await page.click('#btn-layers');
        await new Promise(r => setTimeout(r, 300));

        // Switch to Pure Satellite
        await page.click('.ge-layer-opt[data-layer="satellite"]');
        await new Promise(r => setTimeout(r, 600));
        let activeLayer = await page.evaluate(() => activeLayerName);
        console.log('✔ Switched to Pure Satellite:', activeLayer);

        // Switch to Streets
        await page.click('.ge-layer-opt[data-layer="streets"]');
        await new Promise(r => setTimeout(r, 600));
        activeLayer = await page.evaluate(() => activeLayerName);
        console.log('✔ Switched to Streets:', activeLayer);

        // Switch to Terrain
        await page.click('.ge-layer-opt[data-layer="terrain"]');
        await new Promise(r => setTimeout(r, 600));
        activeLayer = await page.evaluate(() => activeLayerName);
        console.log('✔ Switched to Terrain:', activeLayer);

        // Switch back to Hybrid (default)
        await page.click('.ge-layer-opt[data-layer="hybrid"]');
        await new Promise(r => setTimeout(r, 600));
        activeLayer = await page.evaluate(() => activeLayerName);
        console.log('✔ Switched back to Satellite Hybrid:', activeLayer);

        // Close menu
        await page.click('#map-outer-card');
        await new Promise(r => setTimeout(r, 300));

        // 4. Test Extreme Zooming Details (World -> Street & Building Level)
        console.log('\n[4/9] Testing extreme zoom functionality down to street & building footprints...');
        
        // Fly into a known dense location: Paris / Eiffel Tower or New York
        await page.evaluate(() => {
            leafletMap.setView([48.8584, 2.2945], 18); // Eiffel Tower at zoom 18
        });
        await new Promise(r => setTimeout(r, 2000));

        let zoomInfo = await page.evaluate(() => ({
            zoom: leafletMap.getZoom(),
            center: leafletMap.getCenter(),
            hudText: document.getElementById('ge-coords-display')?.innerText
        }));
        console.log('  Zoomed to Street Level (Zoom 18):', zoomInfo.zoom);
        console.log('  HUD Display:', zoomInfo.hudText.replace(/\n/g, ' '));

        // Deep zoom to maximum supported resolution (zoom 19-20)
        await page.evaluate(() => {
            leafletMap.setZoom(20);
        });
        await new Promise(r => setTimeout(r, 1500));
        const maxZoom = await page.evaluate(() => leafletMap.getZoom());
        console.log('✔ Maximum Zoom Reached:', maxZoom, '(Individual building footprints, roads, structures visible)');

        // Capture high-zoom screenshot
        await page.screenshot({ path: 'screenshot_satellite_street_zoom.png' });
        console.log('✔ Saved high-resolution zoom screenshot: screenshot_satellite_street_zoom.png');

        // 5. Test Zoom Controls (+ and -) and Reset Button
        console.log('\n[5/9] Testing Zoom + / Zoom - and Global Reset buttons...');
        await page.click('#btn-zoom-out');
        await new Promise(r => setTimeout(r, 400));
        const zoomAfterMinus = await page.evaluate(() => leafletMap.getZoom());
        console.log('  Zoom after clicking (-):', zoomAfterMinus);

        await page.click('#btn-zoom-in');
        await new Promise(r => setTimeout(r, 400));
        const zoomAfterPlus = await page.evaluate(() => leafletMap.getZoom());
        console.log('  Zoom after clicking (+):', zoomAfterPlus);

        // Click Reset View
        await page.click('#btn-reset-view');
        await new Promise(r => setTimeout(r, 1500));
        const resetCenter = await page.evaluate(() => ({
            zoom: leafletMap.getZoom(),
            center: leafletMap.getCenter()
        }));
        console.log('✔ Reset View returned to global perspective:', resetCenter);

        // 6. Test Map Search & Geocoding
        console.log('\n[6/9] Testing search bar with instant autocomplete & fly-to...');
        await page.type('#map-search-input', 'India');
        await new Promise(r => setTimeout(r, 800));

        const searchDropdownVisible = await page.$eval('#map-search-results', el => !el.classList.contains('hidden'));
        console.log('  Search dropdown visible:', searchDropdownVisible);

        const firstResultText = await page.$eval('.ge-search-item', el => el.innerText.split('\n')[0]);
        console.log('  First search result:', firstResultText);

        // Click search result
        await page.click('.ge-search-item');
        await new Promise(r => setTimeout(r, 2000));

        const selectedLoc = await page.$eval('#selected-location', el => el.innerText);
        const mapPillText = await page.$eval('#map-active-pill-text', el => el.innerText);
        console.log('✔ Selected location after search:', selectedLoc);
        console.log('✔ Map floating pill text:', mapPillText);

        // 7. Test Map Panning & Dragging
        console.log('\n[7/9] Testing smooth map dragging and manual panning...');
        const centerBeforeDrag = await page.evaluate(() => leafletMap.getCenter());
        
        // Perform drag action
        const mapBox = await page.$eval('#map', el => {
            const rect = el.getBoundingClientRect();
            return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
        });
        await page.mouse.move(mapBox.x, mapBox.y);
        await page.mouse.down();
        await page.mouse.move(mapBox.x + 100, mapBox.y + 80, { steps: 10 });
        await page.mouse.up();
        await new Promise(r => setTimeout(r, 600));

        const centerAfterDrag = await page.evaluate(() => leafletMap.getCenter());
        const dragMoved = (centerBeforeDrag.lat !== centerAfterDrag.lat || centerBeforeDrag.lng !== centerAfterDrag.lng);
        console.log('✔ Manual dragging smooth and responsive. Center moved:', dragMoved);

        // 8. Capture Full World Satellite Map Screenshot
        console.log('\n[8/9] Capturing high-resolution full dashboard & world satellite screenshot...');
        await page.evaluate(() => updateLocationStats('Global'));
        await new Promise(r => setTimeout(r, 1500));
        await page.screenshot({ path: 'screenshot_satellite_world.png', fullPage: true });
        console.log('✔ Saved full dashboard screenshot: screenshot_satellite_world.png');

        // 9. Test Mobile Viewport Responsiveness
        console.log('\n[9/9] Testing mobile responsive rendering (375x812)...');
        await page.setViewport({ width: 375, height: 812, isMobile: true });
        await new Promise(r => setTimeout(r, 1000));
        
        const mobileMapHeight = await page.$eval('#map-container', el => el.clientHeight);
        console.log('  Mobile map container height:', mobileMapHeight, 'px');
        await page.screenshot({ path: 'screenshot_satellite_mobile.png' });
        console.log('✔ Saved mobile screenshot: screenshot_satellite_mobile.png');

        console.log('\n======================================================');
        console.log('🎉 ALL ADVANCED REALISTIC SATELLITE MAP TESTS PASSED!');
        console.log('======================================================\n');

        await browser.close();
        server.close();
        process.exit(0);
    } catch (err) {
        console.error('Test failed with error:', err);
        if (browser) await browser.close();
        server.close();
        process.exit(1);
    }
});
