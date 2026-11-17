# DAV-Project: Movies On Streaming Platforms Analytics & Interactive Dashboard

A comprehensive Data Analysis and Visualisation (DAV) project analysing movies across major streaming platforms (Netflix, Hulu, Prime Video, and Disney+).

---

## 📌 Project Overview

This project provides end-to-end data processing, missing value imputation, statistical analysis, and rich interactive visual dashboards to explore movie catalogs across different streaming services and countries.

### Key Highlights:
- **Google Earth-Style Satellite Mapping (`dashboard.html`)**: High-resolution, photorealistic satellite world map powered by Esri World Imagery (sub-meter resolution up to zoom level 20), stable 2D top-down perspective (no auto-spin), extreme zoom down to building footprints and streets, multi-layer switching (Satellite Hybrid, Pure Satellite, Streets, Topo Terrain), live coordinate HUD tracking, instant geocoding search, full-screen mode, and real-time metric recalculations.
- **Visual Analytics (`all_graphs.html`, `pie_charts.html`)**: Detailed distributions of genres, age classifications, IMDb and Rotten Tomatoes ratings, and platform market share.
- **Data Engineering & Imputation (`prepare_data.py`, `replace_missing_values.py`, etc.)**: Scripts for dataset cleaning, handling missing ratings and demographic values, and generating structured JSON formats.
- **Documentation & Notes**: Includes handwritten lab assignment notes and comprehensive project notes in PDF format.

---

## 📁 Repository Structure

```
DAV-Project/
├── dashboard.html                          # Main interactive streaming dashboard with map & filters
├── all_graphs.html                         # Comprehensive data visualisation graphs
├── pie_charts.html                         # Platform and rating share pie charts
├── prepare_data.py                         # Data preprocessing pipeline
├── replace_missing_values.py               # Imputation logic for missing values
├── analyze_missing.py                      # Missing data analysis script
├── analyze_overlap.py                      # Content overlap analysis between streaming platforms
├── build_all_graphs.py                     # Graph generation automation script
├── deep_dive.py                            # Deep-dive statistical analysis
├── MoviesOnStreamingPlatforms (4).csv      # Cleaned/processed dataset
├── MoviesOnStreamingPlatforms_full.csv     # Full raw streaming dataset
├── cleaned_movies.json                     # Processed movies JSON
├── graphs_data.json                        # Visualisation metrics data
├── movies_data.js                          # Embedded JavaScript dataset for dashboards
├── world_countries.js                      # Local offline GeoJSON boundaries for world countries
├── countries.geo.json                      # GeoJSON dataset of world countries
├── test_satellite_map.js                   # Automated test suite for Google Earth satellite map features
├── verify_dashboard.js                     # Integration test suite for metrics & iframe synchronization
├── Lab_Assignment_3_Handwritten_Notes.pdf  # Handwritten notes for Lab Assignment 3
├── dav project notes.pdf                   # DAV project summary & documentation notes
├── Links_and_Info.md                       # External references, CDN links, and summary
└── README.md                               # Project documentation
```

---

## 🛰️ Google Earth-Style Realistic Satellite Map Experience

The dashboard includes a professional satellite mapping engine:

1. **Photorealistic Sub-Meter Satellite Imagery**:
   - Industry-standard **Esri World Imagery (ArcGIS)** tiles with Maxar, USDA, and USGS sub-meter resolution up to zoom level 20.
   - Dynamic tile streaming that reveals real topography, lakes, forests, highways, neighborhood lanes, and individual building footprints.

2. **Completely Stable Top-Down Perspective**:
   - Zero auto-rotation and zero auto-spin.
   - Fixed top-down 2D perspective with North at the top.
   - Smooth manual panning and zooming without snapping back or unwanted camera wobbling.

3. **Multi-Layer Switcher**:
   - **🛰️ Satellite (Hybrid)**: Esri photorealistic imagery with roads, highways, and place labels.
   - **🌍 Pure Satellite**: Unobstructed satellite photographs without overlays.
   - **🗺️ Detailed Streets**: CartoDB Voyager / OpenStreetMap for roads, buildings, and transit networks.
   - **🏔️ Topographic Terrain**: Elevation contours, mountain relief, and natural features.

4. **Floating Google Earth HUD & Controls**:
   - **Search & Instant Geocoding**: Search for countries, cities, landmarks, or addresses (e.g., "Paris", "Tokyo", "Eiffel Tower", "India") with instant fly-to animation.
   - **Full-Screen Mode**: One-click toggle expanding the map to 100% of the display.
   - **Live Coordinates & Zoom HUD**: Real-time cursor coordinates (Latitude, Longitude) and zoom level readout.
   - **Current Location (GPS)**: Flies smoothly to user coordinates with accuracy indicator.
   - **Interactive Countries & Islands**: Hover glow, movie catalog count tooltips, and click-to-filter syncing with all streaming metrics.

5. **Automated Verification**:
   - Run `node test_satellite_map.js` to execute the 9-point automated Puppeteer test suite verifying stability, zoom, layers, and responsiveness.
   - Run `node verify_dashboard.js` to verify country filtering, data tags, and iframe chart synchronization.

---

## 🚀 Getting Started

### 1. View the Interactive Dashboard
You can open `dashboard.html` directly in any modern web browser:
```bash
# macOS
open dashboard.html

# Linux
xdg-open dashboard.html
```

Or run a local HTTP server:
```bash
python3 -m http.server 8000
```
Then navigate to `http://localhost:8000/dashboard.html` in your browser.

### 2. Run Data Preprocessing Scripts
To re-run the data cleaning and preparation pipelines:
```bash
python3 prepare_data.py
python3 replace_missing_values.py
python3 generate_graphs_data.py
```

---

## 🛠️ Built With

- **HTML5 & CSS3** / **Tailwind CSS**
- **JavaScript (ES6+)**
- **Leaflet.js & CartoDB Tiles** (Interactive geographic mapping)
- **Python 3 & Pandas** (Data wrangling & statistical modeling)

---

## 👥 Author

- GitHub: [@gyan0099](https://github.com/gyan0099)
