
# DAV Project Info & Links

## Files in this directory
1. `dashboard.html` - The main interactive dashboard website containing the world map and data tags.
2. `MoviesOnStreamingPlatforms (4).csv` - The raw data file used to calculate all statistics in the dashboard.

## Important Links & Resources Used
Below are the external libraries and data sources used to build the interactive dashboard:

* **Tailwind CSS (Styling)**: `https://cdn.tailwindcss.com`
* **Leaflet JS (Interactive Maps)**: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.js`
* **Leaflet CSS (Map Styling)**: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.css`
* **World Map Data (GeoJSON)**: Local `world_countries.js` & `countries.geo.json` (fallback: `https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json`)
* **Esri World Imagery (Satellite Tiles)**: `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}` (Sub-meter photorealistic satellite imagery up to zoom level 20)
* **Esri Transportation & Place Labels (Overlays)**: `https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}`
* **Detailed Street Map (CartoDB Voyager)**: `https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png`
* **Topographic Terrain (Esri World Topo)**: `https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}`
* **Nominatim Geocoding API**: `https://nominatim.openstreetmap.org/search` for search & instant fly-to

## Project Summary
* **Rows with missing values**: 4,177
* **Columns with missing values**: 2 (Age, Rotten Tomatoes)
* **18+ Movies**: 23.9%
* **Average Rating**: 53.5/100
* *Dynamic Realistic Satellite Map Integration: The dataset includes authentic Country and Genre attributes across all 9,515 titles. Powered by a stable 2D Google Earth-style satellite mapping engine with sub-meter imagery, no auto-rotation, smooth extreme zooming down to building footprints, live coordinate tracking, instant search geocoding, full-screen mode, and multi-layer switching (Hybrid, Pure Satellite, Streets, Terrain). Every graph, demographic metric, and table dynamically recalculates upon selecting any country or territory.*
