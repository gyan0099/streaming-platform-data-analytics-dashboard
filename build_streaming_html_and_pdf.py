import os
import base64
import subprocess
import shutil

BASE_DIR = "/Users/vedprakash/Desktop/Dav project"
FIG_DIR = os.path.join(BASE_DIR, "presentation_figures")
LOGO_PATH = os.path.join(BASE_DIR, "sru_logo.png")

def get_base64_image(path):
    if not os.path.exists(path):
        return ""
    ext = os.path.splitext(path)[1].lower().replace(".", "")
    if ext == "jpg": ext = "jpeg"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/{ext};base64,{data}"

logo_b64 = get_base64_image(LOGO_PATH)
fig1_b64 = get_base64_image(os.path.join(FIG_DIR, "fig1_boxplot_age_ratings.png"))
fig2_b64 = get_base64_image(os.path.join(FIG_DIR, "fig2_violinplot_density.png"))
fig3_b64 = get_base64_image(os.path.join(FIG_DIR, "fig3_histplot_kde.png"))
fig4_b64 = get_base64_image(os.path.join(FIG_DIR, "fig4_correlation_heatmap.png"))
fig5_b64 = get_base64_image(os.path.join(FIG_DIR, "fig5_platform_catalog_share.png"))
fig6_b64 = get_base64_image(os.path.join(FIG_DIR, "fig6_country_exclusivity.png"))
dash1_b64 = get_base64_image(os.path.join(BASE_DIR, "screenshot.png"))
dash2_b64 = get_base64_image(os.path.join(BASE_DIR, "screenshot_dashboard_india.png"))
map_b64 = get_base64_image(os.path.join(FIG_DIR, "satellite_map_lead_ved.png"))
rep_b64 = get_base64_image(os.path.join(BASE_DIR, "report_screenshot.png"))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Streaming Platforms Dashboard - SR University DAV Project Presentation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');
  
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    background-color: #050811;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #F8FAFC;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  @page {{
    size: 1920px 1080px;
    margin: 0;
  }}
  .slide {{
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    background: #0B132B;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    padding: 35px 50px 30px 50px;
  }}
  
  .slide-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 14px;
    border-bottom: 1px solid #334155;
    margin-bottom: 22px;
  }}
  .header-left {{
    display: flex;
    align-items: center;
    gap: 22px;
  }}
  .logo-box {{
    background: #FFFFFF;
    border-radius: 8px;
    padding: 6px 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #CBD5E1;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  }}
  .logo-box img {{
    height: 48px;
    max-width: 140px;
    object-fit: contain;
  }}
  .header-titles {{
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}
  .sub-tag {{
    font-size: 13px;
    font-weight: 700;
    color: #0EA5E9;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }}
  .main-title {{
    font-size: 24px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.5px;
  }}
  .header-badge {{
    background: #141F38;
    border: 1px solid #38BDF8;
    color: #38BDF8;
    padding: 8px 18px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}

  .slide-footer {{
    margin-top: auto;
    padding-top: 14px;
    border-top: 1px solid #1E293B;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 13px;
    color: #94A3B8;
  }}
  .slide-footer .team {{
    color: #CBD5E1;
    font-weight: 500;
  }}
  .slide-footer .slide-num {{
    color: #38BDF8;
    font-weight: 700;
  }}

  .card {{
    background: #141F38;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 18px 22px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
  }}
  .card-title {{
    font-size: 13px;
    font-weight: 700;
    color: #0EA5E9;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .card-title::before {{
    content: '';
    display: inline-block;
    width: 6px;
    height: 14px;
    background: #0EA5E9;
    border-radius: 2px;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }}
  th {{
    background: #184F90;
    color: #FFFFFF;
    font-weight: 700;
    text-align: left;
    padding: 9px 12px;
  }}
  td {{
    padding: 8px 12px;
    border-bottom: 1px solid #1E293B;
    color: #E2E8F0;
  }}
  tr:nth-child(even) td {{
    background: rgba(16, 26, 48, 0.6);
  }}
  tr:nth-child(odd) td {{
    background: rgba(22, 35, 64, 0.6);
  }}
  .code-font {{
    font-family: 'JetBrains Mono', monospace;
    color: #38BDF8;
  }}
</style>
</head>
<body>

<!-- ======================================================================= -->
<!-- SLIDE 1: COVER PAGE -->
<!-- ======================================================================= -->
<div class="slide" style="justify-content: center; align-items: center; padding: 45px 70px;">
  <div style="width: 100%; height: 100%; background: #0E1730; border: 2px solid #38BDF8; border-radius: 16px; padding: 40px 50px; display: flex; flex-direction: column; justify-content: space-between; position: relative;">
    
    <!-- Top University Banner -->
    <div style="display: flex; align-items: center; gap: 30px; border-bottom: 2px solid #38BDF8; padding-bottom: 25px;">
      <div style="background: white; border-radius: 10px; padding: 8px 20px; display: flex; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
        <img src="{logo_b64}" style="height: 65px; object-fit: contain;">
      </div>
      <div>
        <h1 style="font-size: 26px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.5px; text-transform: uppercase;">SR UNIVERSITY, WARANGAL, TELANGANA</h1>
        <h2 style="font-size: 18px; font-weight: 700; color: #0EA5E9; margin-top: 3px;">SCHOOL OF COMPUTER SCIENCE AND ARTIFICIAL INTELLIGENCE</h2>
        <p style="font-size: 14px; color: #94A3B8; margin-top: 2px;">Department of Artificial Intelligence & Machine Learning • Academic Year 2026–27</p>
      </div>
    </div>

    <!-- Title Block -->
    <div style="text-align: center; margin: 25px 0;">
      <div style="display: inline-block; background: rgba(245, 158, 11, 0.15); border: 1px solid #F59E0B; color: #F59E0B; padding: 6px 18px; border-radius: 20px; font-size: 13px; font-weight: 700; letter-spacing: 1px; margin-bottom: 12px;">
        DATA ANALYTICS AND VISUALIZATION (DAV) • CAPSTONE LAB PROJECT
      </div>
      <h1 style="font-size: 42px; font-weight: 900; color: #FFFFFF; letter-spacing: -1px; line-height: 1.2;">
        STREAMING PLATFORMS DASHBOARD
      </h1>
      <p style="font-size: 18px; color: #38BDF8; font-weight: 700; margin-top: 8px;">
        Movies On Streaming Platforms Analytics, Seaborn Distributions & Realistic Google Earth Satellite Map
      </p>
      <div style="margin-top: 14px; font-size: 14px; color: #CBD5E1; font-weight: 600;">
        Course Code: <span class="code-font" style="color: #F59E0B;">25CAI202PC201</span> &nbsp;|&nbsp; Faculty Evaluation: Mid-Sem Laboratory Presentation
      </div>
    </div>

    <!-- 3 Team Member Cards -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
      
      <!-- Ved Prakash -->
      <div style="background: #141F38; border: 1px solid #38BDF8; border-radius: 12px; padding: 20px 24px;">
        <div style="font-size: 11px; font-weight: 700; color: #38BDF8; letter-spacing: 1px; text-transform: uppercase;">GEOSPATIAL SATELLITE MAP LEAD</div>
        <div style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin-top: 4px;">VED PRAKASH</div>
        <div style="font-size: 14px; font-weight: 700; color: #E2E8F0; margin-top: 2px;">Roll No: <span class="code-font">2503A520Q2</span></div>
        <div style="font-size: 12px; color: #94A3B8; margin-top: 8px; line-height: 1.4;">
          <strong>Responsibilities:</strong> Built Google Earth-style photorealistic satellite map, Leaflet integration, 10-slide deck, report chapters 4 & 5.
        </div>
      </div>

      <!-- Darshan Kumar (LEADER) -->
      <div style="background: #1C284B; border: 2px solid #F59E0B; border-radius: 12px; padding: 20px 24px; box-shadow: 0 0 20px rgba(245, 158, 11, 0.2);">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="font-size: 11px; font-weight: 700; color: #F59E0B; letter-spacing: 1px; text-transform: uppercase;">GROUP LEADER & ARCHITECT</div>
          <span style="background: #F59E0B; color: #000; font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 4px;">LEADER</span>
        </div>
        <div style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin-top: 4px;">DARSHAN KUMAR</div>
        <div style="font-size: 14px; font-weight: 700; color: #E2E8F0; margin-top: 2px;">Roll No: <span class="code-font" style="color: #F59E0B;">2503A520P9</span></div>
        <div style="font-size: 12px; color: #CBD5E1; margin-top: 8px; line-height: 1.4;">
          <strong>Responsibilities:</strong> Project coordination, interactive dashboard architecture, correlation modeling, report chapters 1, 6 & 8.
        </div>
      </div>

      <!-- Sashwat Ghosh -->
      <div style="background: #141F38; border: 1px solid #38BDF8; border-radius: 12px; padding: 20px 24px;">
        <div style="font-size: 11px; font-weight: 700; color: #38BDF8; letter-spacing: 1px; text-transform: uppercase;">DATA CLEANING & EDA LEAD</div>
        <div style="font-size: 20px; font-weight: 800; color: #FFFFFF; margin-top: 4px;">SASHWAT GHOSH</div>
        <div style="font-size: 14px; font-weight: 700; color: #E2E8F0; margin-top: 2px;">Roll No: <span class="code-font">2503A52588</span></div>
        <div style="font-size: 12px; color: #94A3B8; margin-top: 8px; line-height: 1.4;">
          <strong>Responsibilities:</strong> Data cleaning & text sanitization of ratings, boxplot/violin Seaborn scripts, report chapters 2 & 3.
        </div>
      </div>

    </div>

    <!-- Bottom Submission Note -->
    <div style="text-align: center; font-size: 13px; color: #64748B; border-top: 1px solid #1E293B; padding-top: 14px;">
      Submitted to School of Computer Science & Artificial Intelligence, SR University, Warangal | February 2026
    </div>

  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 2: DATA OVERVIEW -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">DATASET ARCHITECTURE, PROVENANCE & SCHEMA SPECIFICATION</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: 32% 66%; gap: 24px; flex: 1;">
    <!-- Left Column: Provenance Card -->
    <div class="card" style="justify-content: space-between;">
      <div class="card-title">DATASET PROVENANCE & SUMMARY</div>
      
      <div style="display: flex; flex-direction: column; gap: 14px; font-size: 13.5px;">
        <div><strong style="color: #38BDF8;">Dataset Name:</strong> <span class="code-font">MoviesOnStreamingPlatforms (4).csv</span></div>
        <div><strong style="color: #38BDF8;">Primary Source:</strong> Kaggle Streaming Platforms Repository</div>
        <div><strong style="color: #38BDF8;">Repository URL:</strong> <a href="#" style="color: #F59E0B; text-decoration: none;">kaggle.com/datasets/ruchi798/movies...</a></div>
        <div><strong style="color: #38BDF8;">Catalog Scope:</strong> Top 4 OTT Services (Netflix, Prime, Hulu, Disney+)</div>
        <div><strong style="color: #38BDF8;">Total Records:</strong> 9,515 Verified Film Titles</div>
        <div><strong style="color: #38BDF8;">Total Attributes:</strong> 17 Feature Columns (Categorical & Numeric)</div>
        <div><strong style="color: #38BDF8;">Target Metrics:</strong> Rotten Tomatoes (0-100%), IMDb (1-10)</div>
        <div><strong style="color: #38BDF8;">Temporal Coverage:</strong> Release Years 1902 to 2021</div>
        <div><strong style="color: #38BDF8;">Exclusivity Rate:</strong> 97.3% Exclusive Titles (9,262 films)</div>
      </div>

      <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10B981; border-radius: 8px; padding: 12px; font-size: 12.5px; color: #A7F3D0; line-height: 1.4;">
        ✔ <strong>Data Governance Notice:</strong> Contains real-world catalog records with international release attributes across all global film producing nations.
      </div>
    </div>

    <!-- Right Column: Schema Table & Preview -->
    <div style="display: flex; flex-direction: column; gap: 20px;">
      
      <!-- Schema Table -->
      <div class="card" style="padding: 16px 20px;">
        <div class="card-title">DATASET ATTRIBUTE DICTIONARY & TYPES</div>
        <table>
          <thead>
            <tr>
              <th>Attribute</th>
              <th>Data Type</th>
              <th>Description / Business Meaning</th>
              <th>Domain Values / Range</th>
            </tr>
          </thead>
          <tbody>
            <tr><td class="code-font">Title</td><td class="code-font" style="color: #F59E0B;">object</td><td>Official movie title name</td><td>9,515 Unique Titles</td></tr>
            <tr><td class="code-font">Year</td><td class="code-font" style="color: #F59E0B;">int64</td><td>Theatrical release year</td><td>1902 – 2021 (Peak: 2017-2020)</td></tr>
            <tr><td class="code-font">Age</td><td class="code-font" style="color: #F59E0B;">object</td><td>Target audience age demographic</td><td>all, 7+, 13+, 16+, 18+</td></tr>
            <tr><td class="code-font">IMDb</td><td class="code-font" style="color: #F59E0B;">float64</td><td>Audience rating score out of 10</td><td>1.0 – 9.3 (Mean: 6.16)</td></tr>
            <tr><td class="code-font">Rotten Tomatoes</td><td class="code-font" style="color: #F59E0B;">float64</td><td>Critic review consensus percentage</td><td>0 – 100% (Mean: 53.55%)</td></tr>
            <tr><td class="code-font">Netflix / Hulu</td><td class="code-font" style="color: #F59E0B;">int64</td><td>Binary streaming availability flag</td><td>0 (Unavailable) or 1 (Available)</td></tr>
            <tr><td class="code-font">Prime / Disney+</td><td class="code-font" style="color: #F59E0B;">int64</td><td>Binary streaming availability flag</td><td>0 (Unavailable) or 1 (Available)</td></tr>
            <tr><td class="code-font">Country / Genres</td><td class="code-font" style="color: #F59E0B;">object</td><td>Origin countries & movie genres</td><td>Comma-separated text tokens</td></tr>
          </tbody>
        </table>
      </div>

      <!-- Raw Preview -->
      <div class="card" style="padding: 16px 20px;">
        <div class="card-title">RAW TRANSACTIONAL DATA PREVIEW (ACTUAL MOVIES SAMPLE)</div>
        <table>
          <thead>
            <tr>
              <th style="background: #1E293B; color: #F59E0B;">Title</th>
              <th style="background: #1E293B; color: #F59E0B;">Year</th>
              <th style="background: #1E293B; color: #F59E0B;">Age</th>
              <th style="background: #1E293B; color: #F59E0B;">IMDb</th>
              <th style="background: #1E293B; color: #F59E0B;">Rotten Tom</th>
              <th style="background: #1E293B; color: #F59E0B;">Netflix</th>
              <th style="background: #1E293B; color: #F59E0B;">Prime</th>
              <th style="background: #1E293B; color: #F59E0B;">Country</th>
            </tr>
          </thead>
          <tbody>
            <tr><td class="code-font">The Irishman</td><td>2019</td><td>18+</td><td>7.8/10</td><td>98/100</td><td>1</td><td>0</td><td>United States</td></tr>
            <tr><td class="code-font">Dangal</td><td>2016</td><td>7+</td><td>8.4/10</td><td>88/100</td><td>1</td><td>0</td><td>India</td></tr>
            <tr><td class="code-font">David Attenborough: Planet</td><td>2020</td><td>7+</td><td>9.0/10</td><td>95/100</td><td>1</td><td>0</td><td>United Kingdom</td></tr>
            <tr><td class="code-font">Lagaan: Once Upon a Time</td><td>2001</td><td>7+</td><td>8.1/10</td><td>94/100</td><td>1</td><td>0</td><td>India, UK</td></tr>
          </tbody>
        </table>
      </div>

    </div>
  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 2 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 3: DATA CLEANING PROCESS -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">DATA PREPROCESSING WORKFLOW, TEXT SANITIZATION & IMPUTATION</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <!-- Top Visual Workflow Pipeline -->
  <div class="card" style="margin-bottom: 22px; padding: 18px 24px;">
    <div class="card-title">END-TO-END DATA CLEANING & PREPARATION PIPELINE</div>
    <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px;">
      
      <div style="background: #0F172A; border: 1px solid #2563EB; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #38BDF8;">STAGE 1</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">CSV Ingestion</div>
        <div style="font-size: 11px; color: #94A3B8;">9,515 raw records ingested via Pandas 2.2 engine</div>
      </div>

      <div style="background: #0F172A; border: 1px solid #2563EB; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #38BDF8;">STAGE 2</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">Schema Audit</div>
        <div style="font-size: 11px; color: #94A3B8;">Age: 4,177, IMDb: 206, Rotten Tomatoes: 7 missing</div>
      </div>

      <div style="background: #0F172A; border: 1px solid #F59E0B; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #F59E0B;">STAGE 3</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">Text Sanitizing</div>
        <div style="font-size: 11px; color: #94A3B8;">Stripped '/100' & '/10' suffix to parse float</div>
      </div>

      <div style="background: #0F172A; border: 1px solid #2563EB; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #38BDF8;">STAGE 4</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">Imputation</div>
        <div style="font-size: 11px; color: #94A3B8;">Categorical modal mapping & target filtration</div>
      </div>

      <div style="background: #0F172A; border: 1px solid #F59E0B; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #F59E0B;">STAGE 5</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">Engineering</div>
        <div style="font-size: 11px; color: #94A3B8;">Rating categories (High/Med/Low) & Exclusivity</div>
      </div>

      <div style="background: #0F172A; border: 1px solid #10B981; border-radius: 8px; padding: 12px 14px;">
        <div style="font-size: 11px; font-weight: 700; color: #10B981;">STAGE 6</div>
        <div style="font-size: 13px; font-weight: 700; color: #FFFFFF; margin: 2px 0;">Gold Store</div>
        <div style="font-size: 11px; color: #94A3B8;">movies_data.js & cleaned_movies.json built</div>
      </div>

    </div>
  </div>

  <!-- Bottom 4 Deep-Dive Preprocessing Cards -->
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
    
    <div class="card">
      <div class="card-title">MISSING DETECTION</div>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">Age Column:</strong><br>4,177 Missing (43.9% of catalog)</div>
        <div><strong style="color: #38BDF8;">IMDb Column:</strong><br>206 Missing (2.16% of catalog)</div>
        <div><strong style="color: #38BDF8;">Rotten Tomatoes:</strong><br>7 Missing (0.07% - near complete)</div>
        <div><strong style="color: #38BDF8;">Country / Directors:</strong><br>254 / 411 Missing respectively</div>
        <div><strong style="color: #10B981;">Status:</strong><br>Audited in analyze_missing.py</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">STRING PARSING & CASTING</div>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">Rotten Tomatoes:</strong><br>Stripped '/100' -> numeric float (98.0)</div>
        <div><strong style="color: #38BDF8;">IMDb Rating:</strong><br>Stripped '/10' -> numeric float (7.8)</div>
        <div><strong style="color: #38BDF8;">Runtime Parsing:</strong><br>Extracted numeric minutes float</div>
        <div><strong style="color: #38BDF8;">Type Conversion:</strong><br>Year & Platform flags cast to int64</div>
        <div><strong style="color: #10B981;">Optimization:</strong><br>Enables Seaborn statistical modeling</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">IMPUTATION & LAB LOGIC</div>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">replace_missing_values:</strong><br>Imputes missing rating values</div>
        <div><strong style="color: #38BDF8;">prepare_data.py:</strong><br>Filters clean subset (5,338 titles)</div>
        <div><strong style="color: #38BDF8;">Age Categorization:</strong><br>Mapped 'all', '7+', '13+', '16+', '18+'</div>
        <div><strong style="color: #38BDF8;">Rating Bins:</strong><br>High (80-100), Med (60-79), Low (&lt;60)</div>
        <div><strong style="color: #10B981;">Validation:</strong><br>Handwritten Lab 3 checklist compliant</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">FEATURE ENGINEERING & TECH</div>
      <div style="display: flex; flex-direction: column; gap: 10px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">Platform Count:</strong><br>Sum of binary flags (Exclusivity Index)</div>
        <div><strong style="color: #38BDF8;">Country Unnesting:</strong><br>Tokenized comma-separated countries</div>
        <div><strong style="color: #38BDF8;">JSON Serializer:</strong><br>Exported cleaned_movies.json & data.js</div>
        <div><strong style="color: #38BDF8;">Python Libraries:</strong><br>Pandas 2.2, NumPy 1.26, Seaborn 0.13</div>
        <div><strong style="color: #10B981;">Web Embedding:</strong><br>Optimized offline array for Leaflet map</div>
      </div>
    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 3 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 4: DATA ANALYSIS (EXECUTIVE BI SUMMARY) -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">EXECUTIVE STREAMING ANALYTICS & STATISTICAL METRICS SUMMARY</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <!-- Top 4 Giant Metric Cards -->
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 22px;">
    
    <div class="card" style="border: 2px solid #38BDF8;">
      <div style="font-size: 12px; font-weight: 700; color: #94A3B8; text-transform: uppercase;">TOTAL MOVIES ANALYZED</div>
      <div style="font-size: 32px; font-weight: 900; color: #38BDF8; margin: 4px 0;">9,515 Titles</div>
      <div style="font-size: 12px; color: #CBD5E1;">Across Netflix, Prime, Hulu, Disney+</div>
    </div>

    <div class="card" style="border: 2px solid #10B981;">
      <div style="font-size: 12px; font-weight: 700; color: #94A3B8; text-transform: uppercase;">PRIME VIDEO CATALOG</div>
      <div style="font-size: 32px; font-weight: 900; color: #10B981; margin: 4px 0;">4,113 Movies</div>
      <div style="font-size: 12px; color: #CBD5E1;">43.2% Global Catalog Share (Lead)</div>
    </div>

    <div class="card" style="border: 2px solid #F59E0B;">
      <div style="font-size: 12px; font-weight: 700; color: #94A3B8; text-transform: uppercase;">AVERAGE CRITIC RATING</div>
      <div style="font-size: 32px; font-weight: 900; color: #F59E0B; margin: 4px 0;">53.55 / 100</div>
      <div style="font-size: 12px; color: #CBD5E1;">Median: 52.0% | IMDb Mean: 6.16</div>
    </div>

    <div class="card" style="border: 2px solid #A855F7;">
      <div style="font-size: 12px; font-weight: 700; color: #94A3B8; text-transform: uppercase;">CONTENT EXCLUSIVITY RATE</div>
      <div style="font-size: 32px; font-weight: 900; color: #A855F7; margin: 4px 0;">97.3% Exclusive</div>
      <div style="font-size: 12px; color: #CBD5E1;">9,262 Movies on Exactly 1 Platform</div>
    </div>

  </div>

  <!-- Bottom 4 Analytical Dimensions -->
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
    
    <div class="card">
      <div class="card-title">PLATFORM SHARE</div>
      <div style="display: flex; flex-direction: column; gap: 9px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">Prime Video (Lead):</strong><br>4,113 titles (43.2%) - Massive library</div>
        <div><strong style="color: #38BDF8;">Netflix (Rank 2):</strong><br>3,695 titles (38.8%) - Premium originals</div>
        <div><strong style="color: #38BDF8;">Hulu (Rank 3):</strong><br>1,047 titles (11.0%) - Curated TV/Film</div>
        <div><strong style="color: #38BDF8;">Disney+ (Specialized):</strong><br>922 titles (9.7%) - Family & franchise</div>
        <div><strong style="color: #38BDF8;">Catalog Overlap:</strong><br>Only 253 titles shared across platforms</div>
        <div style="color: #10B981; font-weight: 600; margin-top: 4px;">Prime Video & Netflix hold 82.0% of films.</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">AGE DEMOGRAPHICS</div>
      <div style="display: flex; flex-direction: column; gap: 9px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">18+ Classification:</strong><br>2,276 titles (42.6% of rated movies)</div>
        <div><strong style="color: #38BDF8;">7+ Classification:</strong><br>1,090 titles (20.4% of rated movies)</div>
        <div><strong style="color: #38BDF8;">13+ Classification:</strong><br>998 titles (18.7% of rated movies)</div>
        <div><strong style="color: #38BDF8;">all Classification:</strong><br>698 titles (13.1% of rated movies)</div>
        <div><strong style="color: #38BDF8;">16+ Classification:</strong><br>276 titles (5.2% of rated movies)</div>
        <div style="color: #10B981; font-weight: 600; margin-top: 4px;">Mature (18+) is the largest single segment.</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">GEOGRAPHIC HUBS</div>
      <div style="display: flex; flex-direction: column; gap: 9px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">United States (Lead):</strong><br>5,888 movie titles (61.9% share)</div>
        <div><strong style="color: #38BDF8;">United Kingdom:</strong><br>960 movie titles (10.1% share)</div>
        <div><strong style="color: #38BDF8;">India (Bollywood/Reg):</strong><br>900 movie titles (9.5% share)</div>
        <div><strong style="color: #38BDF8;">Canada:</strong><br>663 movie titles (7.0% share)</div>
        <div><strong style="color: #38BDF8;">France:</strong><br>456 movie titles (4.8% share)</div>
        <div style="color: #10B981; font-weight: 600; margin-top: 4px;">India is the 3rd largest content creator.</div>
      </div>
    </div>

    <div class="card">
      <div class="card-title">STATISTICAL METRICS</div>
      <div style="display: flex; flex-direction: column; gap: 9px; font-size: 12.5px;">
        <div><strong style="color: #38BDF8;">Mean Rotten Tomatoes:</strong><br>53.55% | Median: 52.0% | Std: 13.20</div>
        <div><strong style="color: #38BDF8;">Mean IMDb Score:</strong><br>6.16 / 10 | Median: 6.30 / 10</div>
        <div><strong style="color: #38BDF8;">Year vs RT Score:</strong><br>Pearson r = -0.02 (Quality independent)</div>
        <div><strong style="color: #38BDF8;">Platform Exclusivity:</strong><br>Negative correlation (r = -0.15 to -0.25)</div>
        <div><strong style="color: #38BDF8;">Seaborn Integration:</strong><br>Boxplot, Violin, Histplot & Heatmap</div>
        <div style="color: #10B981; font-weight: 600; margin-top: 4px;">Licensing exclusivity creates streaming moats.</div>
      </div>
    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 4 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 5: DATA VISUALIZATION: PLATFORM PERFORMANCE & RATINGS -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">DATA VISUALIZATION: SEABORN DISTRIBUTIONS & RATING METRICS</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; flex: 1;">
    
    <!-- Chart 1 -->
    <div class="card" style="padding: 16px;">
      <div class="card-title">FIG 1: BOXPLOT OF SCORES BY AGE</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 350px;">
        <img src="{fig1_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
      <div style="margin-top: 14px; font-size: 12.5px; line-height: 1.5; color: #CBD5E1;">
        <strong style="color: #F59E0B;">Analytical Interpretation:</strong><br>
        • Depicts 5-number summary: Min, Q1, Median, Q3, and Max.<br>
        • Median Rotten Tomatoes score across all age ratings hovers consistently between 50% and 54%.<br>
        • Outliers (dots) reveal extreme critically acclaimed (&gt;90%) or panned films.
      </div>
    </div>

    <!-- Chart 2 -->
    <div class="card" style="padding: 16px;">
      <div class="card-title">FIG 2: VIOLIN PLOT - SCORE DENSITY</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 350px;">
        <img src="{fig2_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
      <div style="margin-top: 14px; font-size: 12.5px; line-height: 1.5; color: #CBD5E1;">
        <strong style="color: #F59E0B;">Analytical Interpretation:</strong><br>
        • Combines mini boxplot with Kernel Density Estimation (KDE) on both sides.<br>
        • Noticeable 'bulge' in the center around 40-55% across all age categories.<br>
        • Confirms the vast majority of catalog titles are average, with thin tails extending to 100%.
      </div>
    </div>

    <!-- Chart 3 -->
    <div class="card" style="padding: 16px;">
      <div class="card-title">FIG 3: HISTOGRAM WITH KDE CURVE</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 350px;">
        <img src="{fig3_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
      <div style="margin-top: 14px; font-size: 12.5px; line-height: 1.5; color: #CBD5E1;">
        <strong style="color: #F59E0B;">Analytical Interpretation:</strong><br>
        • Univariate continuous distribution across 25 bins with smooth KDE overlay.<br>
        • Empirical distribution approximates a Gaussian curve centered at Mean 53.55%.<br>
        • Demonstrates objective, unskewed critic assessment distribution across streaming media.
      </div>
    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 5 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 6: PLOTS AND CONCLUSIONS -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">DEEP-DIVE HEATMAP, CATALOG SHARES & STRATEGIC INDUSTRY CONCLUSIONS</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <!-- Top 3 Plots -->
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 22px;">
    
    <div class="card" style="padding: 14px;">
      <div class="card-title">FIG 4: SEABORN CORRELATION HEATMAP</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 260px;">
        <img src="{fig4_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
    </div>

    <div class="card" style="padding: 14px;">
      <div class="card-title">FIG 5: PLATFORM CATALOG & MARKET SHARE</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 260px;">
        <img src="{fig5_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
    </div>

    <div class="card" style="padding: 14px;">
      <div class="card-title">FIG 6: ORIGIN & CONTENT EXCLUSIVITY</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; height: 260px;">
        <img src="{fig6_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
    </div>

  </div>

  <!-- Bottom 4 Strategic Retail/OTT Conclusions -->
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
    
    <div class="card" style="border-left: 4px solid #38BDF8;">
      <div style="font-size: 12px; font-weight: 700; color: #38BDF8; margin-bottom: 6px;">1. EXCLUSIVITY AS STREAMING MOAT</div>
      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.45;">
        <strong>97.3% of all movie titles (9,262 films)</strong> are exclusive to a single platform.<br><br>
        <span style="color: #94A3B8;"><strong>Conclusion:</strong> Streaming services compete strictly through proprietary licensing barriers rather than shared broad catalogs.</span>
      </div>
    </div>

    <div class="card" style="border-left: 4px solid #F59E0B;">
      <div style="font-size: 12px; font-weight: 700; color: #F59E0B; margin-bottom: 6px;">2. VOLUME VS. ORIGINAL PRODUCTION</div>
      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.45;">
        Prime Video leads global volume (<strong>4,113 titles / 43.2%</strong>), while Netflix emphasizes high-budget proprietary productions (<strong>3,695 titles</strong>).<br><br>
        <span style="color: #94A3B8;"><strong>Conclusion:</strong> Prime focuses on back-catalog depth; Netflix focuses on cultural zeitgeist.</span>
      </div>
    </div>

    <div class="card" style="border-left: 4px solid #10B981;">
      <div style="font-size: 12px; font-weight: 700; color: #10B981; margin-bottom: 6px;">3. DEMOGRAPHIC SPECIALIZATION</div>
      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.45;">
        Mature 18+ content accounts for <strong>42.6% of rated titles</strong>, while Disney+ dominates the 'all' and '7+' family segment (<strong>922 curated titles</strong>).<br><br>
        <span style="color: #94A3B8;"><strong>Conclusion:</strong> OTT platforms exhibit deliberate audience demographic segmentation.</span>
      </div>
    </div>

    <div class="card" style="border-left: 4px solid #A855F7;">
      <div style="font-size: 12px; font-weight: 700; color: #A855F7; margin-bottom: 6px;">4. GLOBAL EXPANSION IN INDIA & UK</div>
      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.45;">
        India (<strong>900 titles</strong>) and the United Kingdom (<strong>960 titles</strong>) represent the largest production hubs outside the United States.<br><br>
        <span style="color: #94A3B8;"><strong>Conclusion:</strong> Regional language localization and Bollywood acquisitions are essential for subscriber retention in Asia.</span>
      </div>
    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 6 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 7: FINAL INTERACTIVE DASHBOARD -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">FINAL INTERACTIVE DASHBOARD SHOWCASE & COUNTRY RECALCULATION</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: 66% 32%; gap: 24px; flex: 1;">
    
    <!-- Main Dashboard Screenshot -->
    <div class="card" style="padding: 16px; justify-content: space-between;">
      <div class="card-title">FIG 7A: STREAMING PLATFORMS INTERACTIVE DASHBOARD (OVERVIEW)</div>
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; border: 1px solid #334155; height: 500px; display: flex; align-items: center; justify-content: center;">
        <img src="{dash1_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>
      <div style="font-size: 12.5px; color: #94A3B8; margin-top: 10px;">
        <strong>Production Interactive Streaming Dashboard:</strong> Integrated with Google Earth-style Esri satellite map, KPI metric tags, dynamic country filters, and real-time demographic recalculations.
      </div>
    </div>

    <!-- Right Side: Filtered View + Feature List -->
    <div style="display: flex; flex-direction: column; gap: 20px;">
      
      <!-- Filtered View -->
      <div class="card" style="padding: 16px;">
        <div class="card-title">FIG 7B: DYNAMIC FILTER (INDIA SELECTED)</div>
        <div style="background: #0B132B; border-radius: 8px; overflow: hidden; border: 1px solid #334155; height: 260px; display: flex; align-items: center; justify-content: center;">
          <img src="{dash2_b64}" style="width: 100%; height: 100%; object-fit: contain;">
        </div>
      </div>

      <!-- Features -->
      <div class="card" style="padding: 16px; flex: 1;">
        <div class="card-title">CORE DASHBOARD CAPABILITIES</div>
        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 12.5px;">
          <div><strong style="color: #38BDF8;">Global Country Filtering:</strong><br>Clicking any country instantly recalculates title count, platform share, and ratings.</div>
          <div><strong style="color: #38BDF8;">Multi-Layer Satellite Map:</strong><br>Esri World Imagery, CartoDB streets, and topographic terrain switching.</div>
          <div><strong style="color: #38BDF8;">Dynamic Platform Slicers:</strong><br>Interactive toggles for Netflix, Hulu, Prime Video, and Disney+.</div>
          <div><strong style="color: #10B981;">Zero-Latency Offline Architecture:</strong><br>Embedded GeoJSON boundaries & movies_data.js for high-speed client rendering.</div>
        </div>
      </div>

    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 7 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 8: PROJECT ARCHITECTURE AND MAP DESIGN -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">PROJECT ARCHITECTURE & REALISTIC SATELLITE MAP (LEAD: VED PRAKASH)</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: 44% 54%; gap: 24px; flex: 1;">
    
    <!-- Left: System Architecture Flow -->
    <div class="card" style="justify-content: space-between;">
      <div class="card-title">END-TO-END SYSTEM ARCHITECTURE & STACK</div>
      
      <div style="display: flex; flex-direction: column; gap: 10px;">
        
        <div style="background: #0F172A; border-left: 3px solid #2563EB; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #2563EB;">DATA INGESTION LAYER [9,515 Movies CSV Engine]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">Ingests raw streaming catalogs, parses 17 schema fields and metadata.</div>
        </div>

        <div style="background: #0F172A; border-left: 3px solid #38BDF8; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #38BDF8;">PREPROCESSING & IMPUTATION [Pandas / NumPy / Python]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">Cleans Rotten Tomatoes text, handles missing Age ratings, builds JSON data.</div>
        </div>

        <div style="background: #0F172A; border-left: 3px solid #10B981; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #10B981;">STATISTICAL & EDA ENGINE [Seaborn 0.13 / Matplotlib]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">Computes boxplots, violin plots, KDE distributions, and correlation matrices.</div>
        </div>

        <div style="background: #0F172A; border-left: 3px solid #F59E0B; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #F59E0B;">GEOSPATIAL SATELLITE ENGINE [Leaflet JS / Esri Imagery]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">Sub-meter photorealistic satellite tiles, stable 2D top-down view, HUD.</div>
        </div>

        <div style="background: #0F172A; border-left: 3px solid #A855F7; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #A855F7;">INTERACTIVE DASHBOARD LAYER [HTML5 / Tailwind / Chart.js]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">Reactive dashboard UI, dynamic country click filtering, iframe sync.</div>
        </div>

        <div style="background: #0F172A; border-left: 3px solid #184F90; border-radius: 6px; padding: 8px 12px;">
          <div style="font-size: 11px; font-weight: 700; color: #38BDF8;">DOCUMENTATION & REPORTS [DAV Project Report (.docx)]</div>
          <div style="font-size: 11.5px; color: #CBD5E1;">8-chapter university report, lab viva notes, automated test suites.</div>
        </div>

      </div>

      <div style="background: rgba(14, 165, 233, 0.1); border: 1px solid #0EA5E9; border-radius: 8px; padding: 10px; font-size: 11.5px; color: #38BDF8; font-weight: 600;">
        Technology Stack: Python 3.14 | Pandas | NumPy | Seaborn | Matplotlib | Leaflet.js | Esri GIS | Tailwind CSS
      </div>
    </div>

    <!-- Right: Dedicated Realistic Satellite Map Design Section (Ved Prakash) -->
    <div class="card" style="padding: 16px; justify-content: space-between;">
      
      <!-- Prominent Attribution Banner -->
      <div style="background: #1C284B; border: 2px solid #F59E0B; border-radius: 8px; padding: 10px 16px; text-align: center; box-shadow: 0 0 15px rgba(245, 158, 11, 0.25);">
        <span style="font-size: 13px; font-weight: 800; color: #F59E0B; letter-spacing: 0.5px;">
          GEOGRAPHICAL SATELLITE MAP DESIGNED & INTEGRATED BY: VED PRAKASH (2503A520Q2)
        </span>
      </div>

      <!-- Map Screenshot -->
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; border: 1px solid #334155; height: 360px; margin: 12px 0; display: flex; align-items: center; justify-content: center;">
        <img src="{map_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>

      <!-- Map Details -->
      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.5;">
        <strong style="color: #38BDF8;">Satellite Mapping Engine Specifications (Ved Prakash):</strong><br>
        • Esri World Imagery (ArcGIS) tiles: Sub-meter photorealistic imagery up to zoom level 20 (reveals terrain, roads, building footprints).<br>
        • Stable 2D Top-Down View: Fixed North perspective with zero auto-rotation, zero auto-spin, and smooth inertial panning.<br>
        • Multi-Layer Controls: Hybrid Satellite, Pure Satellite, Street Map, and Topographic Terrain with Nominatim Instant Search.
      </div>

    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 8 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 9: ACADEMIC PROJECT REPORT AND DOCUMENTATION -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">ACADEMIC DOCUMENTATION & 8-CHAPTER UNIVERSITY REPORT ALIGNMENT</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: 42% 56%; gap: 24px; flex: 1;">
    
    <!-- Left: Report Screenshots -->
    <div class="card" style="padding: 16px; justify-content: space-between;">
      <div class="card-title">AUTHENTIC REPORT & LAB ARTIFACTS</div>
      
      <div style="background: #0B132B; border-radius: 8px; overflow: hidden; border: 1px solid #334155; height: 380px; display: flex; align-items: center; justify-content: center;">
        <img src="{rep_b64}" style="width: 100%; height: 100%; object-fit: contain;">
      </div>

      <div style="font-size: 12px; color: #CBD5E1; line-height: 1.45; margin-top: 10px;">
        <strong style="color: #F59E0B;">Official Academic Documentation & Lab Artifacts:</strong><br>
        • Formatted strictly in accordance with SR University CSAI guidelines.<br>
        • Includes handwritten notes (Lab_Assignment_3_Handwritten_Notes.pdf), comprehensive project notes (dav project notes.pdf), viva revision cheat-sheets, and automated Puppeteer test suites (test_satellite_map.js, verify_dashboard.js).
      </div>
    </div>

    <!-- Right: Chapter Breakdown -->
    <div class="card" style="padding: 16px; justify-content: space-between;">
      <div class="card-title">UNIVERSITY REPORT CHAPTER-BY-CHAPTER COMPLIANCE</div>
      
      <table>
        <thead>
          <tr>
            <th style="width: 18%;">Chapter</th>
            <th style="width: 42%;">Formal Chapter Title</th>
            <th style="width: 40%;">Academic Scope & Coverage</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="code-font">Chapter 1</td><td style="font-weight: 600;">Introduction & OTT Landscape</td><td>Streaming platform growth, catalog discovery problem</td></tr>
          <tr><td class="code-font">Chapter 2</td><td style="font-weight: 600;">Dataset Description & Ingestion</td><td>Kaggle dataset origin, 17 attributes, 9,515 titles</td></tr>
          <tr><td class="code-font">Chapter 3</td><td style="font-weight: 600;">Exploratory Data Analysis & ETL</td><td>Text sanitization of Rotten Tomatoes, Age imputation</td></tr>
          <tr style="background: rgba(245, 158, 11, 0.1);"><td class="code-font" style="color: #F59E0B;">Chapter 4</td><td style="font-weight: 700; color: #F59E0B;">Realistic Satellite World Map</td><td><strong>Lead: Ved Prakash</strong> – Esri sub-meter tiles & Leaflet GIS</td></tr>
          <tr style="background: rgba(14, 165, 233, 0.1);"><td class="code-font" style="color: #38BDF8;">Chapter 5</td><td style="font-weight: 700; color: #38BDF8;">Interactive Dashboard Architecture</td><td><strong>Lead: Darshan Kumar</strong> – Reactive UI & country filters</td></tr>
          <tr><td class="code-font">Chapter 6</td><td style="font-weight: 600;">Empirical Findings & Viva Q/A</td><td>Boxplots, violins, KDE curves, Pearson correlation</td></tr>
          <tr><td class="code-font">Chapter 7</td><td style="font-weight: 600;">System Limitations & Future Scope</td><td>Live streaming API telemetry, personalized ML engine</td></tr>
          <tr><td class="code-font">Chapter 8</td><td style="font-weight: 600;">Conclusion & Academic References</td><td>Deliverables summary and formal IEEE citations</td></tr>
        </tbody>
      </table>

      <div style="background: rgba(14, 165, 233, 0.1); border: 1px solid #0EA5E9; border-radius: 8px; padding: 10px 14px; font-size: 12px; color: #38BDF8; font-weight: 600;">
        Project Artifacts & Links: GitHub (@gyan0099) | Live Dashboard (dashboard.html) | Word Report (.docx) | Presentation (.pptx & .pdf)
      </div>

    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 9 of 10</span>
  </div>
</div>

<!-- ======================================================================= -->
<!-- SLIDE 10: TEAM CONTRIBUTIONS, CONCLUSION & CLOSING -->
<!-- ======================================================================= -->
<div class="slide">
  <div class="slide-header">
    <div class="header-left">
      <div class="logo-box"><img src="{logo_b64}"></div>
      <div class="header-titles">
        <span class="sub-tag">SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201</span>
        <span class="main-title">TEAM RESPONSIBILITY MATRIX, PROJECT CONCLUSION & ACKNOWLEDGMENTS</span>
      </div>
    </div>
    <div class="header-badge">STREAMING PLATFORMS</div>
  </div>

  <div style="display: grid; grid-template-columns: 62% 36%; gap: 24px; flex: 1;">
    
    <!-- Left: Detailed Team Cards -->
    <div class="card" style="justify-content: space-between;">
      <div class="card-title">INDIVIDUAL TEAM CONTRIBUTIONS & RESPONSIBILITY MATRIX</div>
      
      <div style="display: flex; flex-direction: column; gap: 14px;">
        
        <!-- Ved Prakash -->
        <div style="background: #0F172A; border: 1px solid #38BDF8; border-radius: 8px; padding: 12px 16px;">
          <div style="font-size: 13.5px; font-weight: 800; color: #FFFFFF;">
            VED PRAKASH &nbsp;|&nbsp; <span class="code-font">2503A520Q2</span> &nbsp;•&nbsp; <span style="color: #38BDF8;">GEOSPATIAL SATELLITE MAP LEAD</span>
          </div>
          <div style="font-size: 11.5px; color: #CBD5E1; margin-top: 6px; line-height: 1.45;">
            • <strong>Realistic Satellite Engine:</strong> Integrated Esri World Imagery (ArcGIS) sub-meter tiles into dashboard.html with zoom level 20.<br>
            • <strong>Map Stability & Controls:</strong> Engineered stable 2D top-down view (zero auto-rotation/auto-spin), full-screen toggle, & coordinate HUD.<br>
            • <strong>Deck Synthesis:</strong> Spearheaded the 10-slide academic PowerPoint presentation, data visualization layout, and theme architecture.<br>
            • <strong>Report Authoring:</strong> Authored Chapter 4 (Geospatial Satellite Integration) and Chapter 5 (Interactive Dashboard Architecture).
          </div>
        </div>

        <!-- Darshan Kumar -->
        <div style="background: #1C284B; border: 2px solid #F59E0B; border-radius: 8px; padding: 12px 16px;">
          <div style="font-size: 13.5px; font-weight: 800; color: #FFFFFF;">
            DARSHAN KUMAR &nbsp;|&nbsp; <span class="code-font" style="color: #F59E0B;">2503A520P9</span> &nbsp;•&nbsp; <span style="color: #F59E0B;">GROUP LEADER & SYSTEM ARCHITECT</span>
          </div>
          <div style="font-size: 11.5px; color: #CBD5E1; margin-top: 6px; line-height: 1.45;">
            • <strong>Project Leadership:</strong> Coordinated team milestones, task allocation, code repository integration, and academic reviews.<br>
            • <strong>Dashboard Architecture:</strong> Designed reactive country-filter recalculation engine, multi-platform slicers, and summary cards.<br>
            • <strong>Statistical Modeling:</strong> Executed Pearson correlation matrix, content exclusivity modeling, and streaming retail conclusions.<br>
            • <strong>Report Authoring:</strong> Authored Chapter 1 (Introduction), Chapter 6 (Empirical Findings & Viva Q/A), and Chapter 8 (Conclusion).
          </div>
        </div>

        <!-- Sashwat Ghosh -->
        <div style="background: #0F172A; border: 1px solid #38BDF8; border-radius: 8px; padding: 12px 16px;">
          <div style="font-size: 13.5px; font-weight: 800; color: #FFFFFF;">
            SASHWAT GHOSH &nbsp;|&nbsp; <span class="code-font">2503A52588</span> &nbsp;•&nbsp; <span style="color: #38BDF8;">DATA CLEANING & EDA LEAD</span>
          </div>
          <div style="font-size: 11.5px; color: #CBD5E1; margin-top: 6px; line-height: 1.45;">
            • <strong>ETL & Text Sanitization:</strong> Engineered prepare_data.py to strip '/100' string suffixes from Rotten Tomatoes into clean numeric floats.<br>
            • <strong>Missing Value Imputation:</strong> Developed replace_missing_values.py to analyze and impute 4,177 unrated Age demographic entries.<br>
            • <strong>Seaborn Visualization:</strong> Implemented boxplot, violin plot, and histogram KDE charts matching Lab Assignment 3 specifications.<br>
            • <strong>Report Authoring:</strong> Authored Chapter 2 (Dataset Description) and Chapter 3 (Exploratory Data Analysis).
          </div>
        </div>

      </div>
    </div>

    <!-- Right: Conclusion & Thank You -->
    <div style="display: flex; flex-direction: column; gap: 20px;">
      
      <!-- Conclusion Card -->
      <div class="card" style="padding: 16px;">
        <div class="card-title">EXECUTIVE PROJECT CONCLUSION</div>
        <div style="font-size: 12.5px; color: #CBD5E1; line-height: 1.5;">
          <strong style="color: #F59E0B;">Summary of Academic & Technical Impact:</strong><br><br>
          <strong>1. Technical Mastery:</strong> Delivered full-stack data analytics from 9,515 raw film records to an interactive Google Earth-style satellite map.<br><br>
          <strong>2. Statistical Rigor:</strong> Applied Seaborn boxplots, violin plots, KDE distributions, and correlation heatmaps strictly fulfilling Lab 3.<br><br>
          <strong>3. Business Relevance:</strong> Uncovered key OTT dynamics (97.3% catalog exclusivity, Prime Video volume lead, and India's production surge).
        </div>
      </div>

      <!-- Thank You Card -->
      <div class="card" style="padding: 20px; flex: 1; justify-content: center; text-align: center; background: #0E1730; border: 2px solid #38BDF8;">
        <h2 style="font-size: 28px; font-weight: 900; color: #FFFFFF; letter-spacing: -0.5px;">THANK YOU!</h2>
        <p style="font-size: 13.5px; color: #94A3B8; margin-top: 8px;">
          We welcome questions, evaluations, and guidance from our faculty and evaluators.
        </p>
        <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid #1E293B; font-size: 12.5px; color: #38BDF8; font-weight: 700; line-height: 1.4;">
          SR UNIVERSITY, WARANGAL<br>
          School of Computer Science & Artificial Intelligence<br>
          <span style="color: #94A3B8; font-weight: 500;">Course: Data Analytics & Visualization (25CAI202PC201) • 2026–27</span>
        </div>
      </div>

    </div>

  </div>

  <div class="slide-footer">
    <span>Data Analytics & Visualization (DAV) • Academic Year 2026–27</span>
    <span class="team">Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)</span>
    <span class="slide-num">Slide 10 of 10</span>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(BASE_DIR, "presentation_deck.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"presentation_deck.html generated successfully ({os.path.getsize(html_path):,} bytes).")
