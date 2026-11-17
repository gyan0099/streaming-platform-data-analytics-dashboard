import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = "/Users/vedprakash/Desktop/Dav project"
FIG_DIR = os.path.join(BASE_DIR, "presentation_figures")
LOGO_PATH = os.path.join(BASE_DIR, "sru_logo.png")

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Theme Colors (SR University & Modern Streaming Dark Theme)
DARK_BG = RGBColor(11, 19, 43)        # #0B132B Deep Midnight Navy
CARD_BG = RGBColor(20, 31, 56)        # #141F38 Slate Blue Card
CARD_BORDER = RGBColor(56, 189, 248)  # #38BDF8 Cyan Accent
BORDER_MUTED = RGBColor(51, 65, 85)   # #334155
SRU_NAVY = RGBColor(24, 79, 144)      # #184F90 Official SRU Navy
SRU_BLUE = RGBColor(37, 99, 235)      # #2563EB Cobalt Blue
CYAN_TEXT = RGBColor(14, 165, 233)    # #0EA5E9 Bright Cyan
TEXT_WHITE = RGBColor(255, 255, 255)
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8 Slate Gray
TEXT_BODY = RGBColor(226, 232, 240)   # #E2E8F0 Light Gray
GOLD = RGBColor(245, 158, 11)         # #F59E0B Amber Gold
EMERALD = RGBColor(16, 185, 129)      # #10B981 Emerald Green
PURPLE = RGBColor(168, 85, 247)       # #A855F7 Purple
RED_NETFLIX = RGBColor(229, 9, 20)    # #E50914

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    return bg

def add_header_and_footer(slide, slide_num, title_text, category_text="SR UNIVERSITY • SCHOOL OF CSAI • COURSE 25CAI202PC201"):
    # Logo container box
    logo_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.28), Inches(1.4), Inches(0.6))
    logo_card.fill.solid()
    logo_card.fill.fore_color.rgb = RGBColor(255, 255, 255)
    logo_card.line.color.rgb = RGBColor(203, 213, 225)
    logo_card.line.width = Pt(1)

    if os.path.exists(LOGO_PATH):
        slide.shapes.add_picture(LOGO_PATH, Inches(0.66), Inches(0.32), width=Inches(1.28), height=Inches(0.52))

    # Header Titles
    tb = slide.shapes.add_textbox(Inches(2.15), Inches(0.25), Inches(8.4), Inches(0.68))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p1 = tf.paragraphs[0]
    p1.text = category_text.upper()
    p1.font.name = "Arial"
    p1.font.size = Pt(8.5)
    p1.font.bold = True
    p1.font.color.rgb = CYAN_TEXT

    p2 = tf.add_paragraph()
    p2.text = title_text
    p2.font.name = "Arial"
    p2.font.size = Pt(16.5)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    # Top Right Project Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(0.32), Inches(2.13), Inches(0.5))
    badge.fill.solid()
    badge.fill.fore_color.rgb = CARD_BG
    badge.line.color.rgb = CARD_BORDER
    badge.line.width = Pt(1)
    btf = badge.text_frame
    btf.word_wrap = True
    bp = btf.paragraphs[0]
    bp.alignment = PP_ALIGN.CENTER
    bp.text = "STREAMING PLATFORMS"
    bp.font.name = "Arial"
    bp.font.size = Pt(9)
    bp.font.bold = True
    bp.font.color.rgb = CYAN_TEXT

    # Header Divider Line
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(1.02), Inches(12.133), Pt(1))
    line.fill.solid()
    line.fill.fore_color.rgb = BORDER_MUTED
    line.line.fill.background()

    # Footer Divider Line
    line_f = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.04), Inches(12.133), Pt(1))
    line_f.fill.solid()
    line_f.fill.fore_color.rgb = RGBColor(30, 41, 59)
    line_f.line.fill.background()

    # Footer Left
    ftb = slide.shapes.add_textbox(Inches(0.6), Inches(7.08), Inches(4.5), Inches(0.35))
    ftf = ftb.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "Data Analytics & Visualization (DAV) • Academic Year 2026–27"
    fp.font.name = "Arial"
    fp.font.size = Pt(8.5)
    fp.font.color.rgb = TEXT_MUTED

    # Footer Center (Team)
    ctb = slide.shapes.add_textbox(Inches(4.6), Inches(7.08), Inches(5.8), Inches(0.35))
    ctf = ctb.text_frame
    cp = ctf.paragraphs[0]
    cp.alignment = PP_ALIGN.CENTER
    cp.text = "Ved Prakash (2503A520Q2) | Darshan Kumar - Group Leader (2503A520P9) | Sashwat Ghosh (2503A52588)"
    cp.font.name = "Arial"
    cp.font.size = Pt(8.5)
    cp.font.color.rgb = TEXT_MUTED

    # Footer Right (Slide Number)
    rtb = slide.shapes.add_textbox(Inches(11.2), Inches(7.08), Inches(1.5), Inches(0.35))
    rtf = rtb.text_frame
    rp = rtf.paragraphs[0]
    rp.alignment = PP_ALIGN.RIGHT
    rp.text = f"Slide {slide_num} of 10"
    rp.font.name = "Arial"
    rp.font.size = Pt(9)
    rp.font.bold = True
    rp.font.color.rgb = CYAN_TEXT

def create_card(slide, left, top, width, height, title="", fill_color=CARD_BG, border_color=None):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.color.rgb = BORDER_MUTED
        card.line.width = Pt(0.75)
    
    if title:
        tb = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.12), width - Inches(0.36), Inches(0.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.name = "Arial"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = CYAN_TEXT
    return card

# ==============================================================================
# SLIDE 1: COVER PAGE
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)
set_slide_background(slide1)

frame = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(0.5), Inches(12.133), Inches(6.5))
frame.fill.solid()
frame.fill.fore_color.rgb = RGBColor(14, 23, 48)
frame.line.color.rgb = CARD_BORDER
frame.line.width = Pt(1.5)

# Logo Box
logo_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.85), Inches(2.2), Inches(0.95))
logo_box.fill.solid()
logo_box.fill.fore_color.rgb = RGBColor(255, 255, 255)
logo_box.line.color.rgb = RGBColor(203, 213, 225)
logo_box.line.width = Pt(1)
if os.path.exists(LOGO_PATH):
    slide1.shapes.add_picture(LOGO_PATH, Inches(1.1), Inches(0.92), width=Inches(2.0), height=Inches(0.81))

# University & Department Info
univ_box = slide1.shapes.add_textbox(Inches(3.4), Inches(0.82), Inches(8.9), Inches(1.0))
utf = univ_box.text_frame
utf.word_wrap = True
up1 = utf.paragraphs[0]
up1.text = "SR UNIVERSITY, WARANGAL, TELANGANA"
up1.font.name = "Arial"
up1.font.size = Pt(16)
up1.font.bold = True
up1.font.color.rgb = TEXT_WHITE

up2 = utf.add_paragraph()
up2.text = "SCHOOL OF COMPUTER SCIENCE AND ARTIFICIAL INTELLIGENCE"
up2.font.name = "Arial"
up2.font.size = Pt(12)
up2.font.bold = True
up2.font.color.rgb = CYAN_TEXT

up3 = utf.add_paragraph()
up3.text = "Department of Artificial Intelligence & Machine Learning • Academic Year 2026–27"
up3.font.name = "Arial"
up3.font.size = Pt(10)
up3.font.color.rgb = TEXT_MUTED

# Divider
div1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.95), Inches(11.333), Pt(1.5))
div1.fill.solid()
div1.fill.fore_color.rgb = RGBColor(56, 189, 248)
div1.line.fill.background()

# Hero Title Block
hero_box = slide1.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(11.333), Inches(1.7))
htf = hero_box.text_frame
htf.word_wrap = True
hp0 = htf.paragraphs[0]
hp0.text = "DATA ANALYTICS AND VISUALIZATION (DAV) • CAPSTONE LAB PROJECT"
hp0.font.name = "Arial"
hp0.font.size = Pt(11)
hp0.font.bold = True
hp0.font.color.rgb = GOLD

hp1 = htf.add_paragraph()
hp1.text = "STREAMING PLATFORMS DASHBOARD"
hp1.font.name = "Arial"
hp1.font.size = Pt(26)
hp1.font.bold = True
hp1.font.color.rgb = TEXT_WHITE

hp2 = htf.add_paragraph()
hp2.text = "Movies On Streaming Platforms Analytics, Seaborn Distributions & Realistic Google Earth Satellite Map"
hp2.font.name = "Arial"
hp2.font.size = Pt(12)
hp2.font.color.rgb = CYAN_TEXT

hp3 = htf.add_paragraph()
hp3.text = "Course: Data Analytics & Visualization | Course Code: 25CAI202PC201 | Faculty Evaluation: Mid-Sem Laboratory Presentation"
hp3.font.name = "Arial"
hp3.font.size = Pt(10.5)
hp3.font.color.rgb = TEXT_MUTED

# 3 Team Cards
team_data = [
    ("VED PRAKASH", "2503A520Q2", "GEOSPATIAL SATELLITE MAP LEAD", "Google Earth-Style Esri Satellite Map, Leaflet Integration, 10-Slide Deck, Report Ch 4-5", CARD_BG, CARD_BORDER),
    ("DARSHAN KUMAR", "2503A520P9", "GROUP LEADER & SYSTEM ARCHITECT", "Project Coordination, Interactive Dashboard Architecture, Statistical Modeling, Report Ch 1,6,8", RGBColor(28, 40, 75), GOLD),
    ("SASHWAT GHOSH", "2503A52588", "DATA CLEANING & EDA LEAD", "Data Preprocessing, Rating Sanitization, Boxplot/Violin/Heatmap Seaborn Charts, Report Ch 2-3", CARD_BG, CARD_BORDER),
]

card_w = Inches(3.64)
card_h = Inches(2.25)
gap = Inches(0.2)
start_x = Inches(1.0)
y_pos = Inches(4.0)

for i, (name, roll, role, contrib, bg_col, bdr_col) in enumerate(team_data):
    cx = start_x + i * (card_w + gap)
    c_shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, y_pos, card_w, card_h)
    c_shape.fill.solid()
    c_shape.fill.fore_color.rgb = bg_col
    c_shape.line.color.rgb = bdr_col
    c_shape.line.width = Pt(1.5 if bdr_col == GOLD else 1)

    ctb = slide1.shapes.add_textbox(cx + Inches(0.15), y_pos + Inches(0.15), card_w - Inches(0.3), card_h - Inches(0.3))
    ctf = ctb.text_frame
    ctf.word_wrap = True

    p_badge = ctf.paragraphs[0]
    p_badge.text = role
    p_badge.font.name = "Arial"
    p_badge.font.size = Pt(8.5)
    p_badge.font.bold = True
    p_badge.font.color.rgb = GOLD if bdr_col == GOLD else CYAN_TEXT

    p_name = ctf.add_paragraph()
    p_name.text = name
    p_name.font.name = "Arial"
    p_name.font.size = Pt(14)
    p_name.font.bold = True
    p_name.font.color.rgb = TEXT_WHITE

    p_roll = ctf.add_paragraph()
    p_roll.text = f"Roll No: {roll}"
    p_roll.font.name = "Arial"
    p_roll.font.size = Pt(10)
    p_roll.font.bold = True
    p_roll.font.color.rgb = TEXT_BODY

    p_con = ctf.add_paragraph()
    p_con.text = f"Responsibilities:\n{contrib}"
    p_con.font.name = "Arial"
    p_con.font.size = Pt(8.5)
    p_con.font.color.rgb = TEXT_MUTED

# Footer Note on Cover
cf_tb = slide1.shapes.add_textbox(Inches(1.0), Inches(6.35), Inches(11.333), Inches(0.5))
cftf = cf_tb.text_frame
cfp = cftf.paragraphs[0]
cfp.alignment = PP_ALIGN.CENTER
cfp.text = "Submitted to School of Computer Science & Artificial Intelligence, SR University, Warangal | February 2026"
cfp.font.name = "Arial"
cfp.font.size = Pt(9)
cfp.font.color.rgb = TEXT_MUTED

print("Slide 1 generated.")

# ==============================================================================
# SLIDE 2: DATA OVERVIEW
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
set_slide_background(slide2)
add_header_and_footer(slide2, 2, "DATASET ARCHITECTURE, PROVENANCE & SCHEMA SPECIFICATION")

# Left Column: Metadata & Provenance Card
create_card(slide2, Inches(0.6), Inches(1.18), Inches(4.2), Inches(5.65), "DATASET PROVENANCE & SUMMARY")
meta_tb = slide2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(3.8), Inches(5.0))
mtf = meta_tb.text_frame
mtf.word_wrap = True

meta_items = [
    ("Dataset Name", "MoviesOnStreamingPlatforms (4).csv"),
    ("Primary Source", "Kaggle Streaming Platforms Repository"),
    ("Repository URL", "kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disney"),
    ("Catalog Scope", "Global Movie Titles across Top 4 OTT Services"),
    ("Platforms Included", "Netflix, Hulu, Prime Video, Disney+"),
    ("Total Records", "9,515 Verified Film Titles"),
    ("Total Attributes", "17 Feature Columns (Categorical & Numeric)"),
    ("Target Metrics", "Rotten Tomatoes (0-100%), IMDb (1-10)"),
    ("Temporal Range", "Release Years spanning 1902 to 2021"),
    ("Data Status", "Standardized, Processed, Imputed")
]

for idx, (label, val) in enumerate(meta_items):
    p = mtf.paragraphs[0] if idx == 0 else mtf.add_paragraph()
    p.text = f"• {label}: "
    p.font.name = "Arial"
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = CYAN_TEXT
    run = p.add_run()
    run.text = val
    run.font.name = "Arial"
    run.font.size = Pt(8.5)
    run.font.bold = False
    run.font.color.rgb = TEXT_BODY

# Right Top: Attribute Schema Table
create_card(slide2, Inches(5.0), Inches(1.18), Inches(7.733), Inches(3.1), "DATASET ATTRIBUTE DICTIONARY & TYPES")
schema_table_shape = slide2.shapes.add_table(9, 4, Inches(5.15), Inches(1.58), Inches(7.433), Inches(2.55))
st = schema_table_shape.table
st.columns[0].width = Inches(1.5)
st.columns[1].width = Inches(1.1)
st.columns[2].width = Inches(2.833)
st.columns[3].width = Inches(2.0)

headers = ["Attribute", "Data Type", "Description / Definition", "Domain Values / Range"]
for j, h in enumerate(headers):
    cell = st.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = SRU_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

schema_rows = [
    ("Title", "object", "Official movie title name", "9,515 Unique Titles"),
    ("Year", "int64", "Theatrical release year", "1902 – 2021 (Peak: 2017-2020)"),
    ("Age", "object", "Target audience age demographic", "all, 7+, 13+, 16+, 18+"),
    ("IMDb", "float64", "Audience rating score out of 10", "1.0 – 9.3 (Mean: 6.16)"),
    ("Rotten Tomatoes", "float64", "Critic consensus score percentage", "0 – 100% (Mean: 53.55%)"),
    ("Netflix / Hulu", "int64", "Binary streaming availability flag", "0 (Not Available) or 1 (Available)"),
    ("Prime / Disney+", "int64", "Binary streaming availability flag", "0 (Not Available) or 1 (Available)"),
    ("Country / Genres", "object", "Origin countries & movie genres", "Comma-separated text tokens")
]

for i, row in enumerate(schema_rows):
    for j, val in enumerate(row):
        cell = st.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(16, 26, 48) if i % 2 == 0 else RGBColor(22, 35, 64)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(8)
        p.font.color.rgb = TEXT_WHITE if j == 0 else (CYAN_TEXT if j == 1 else TEXT_BODY)

# Right Bottom: Raw Data Preview Table (First 4 rows of MoviesOnStreamingPlatforms.csv)
create_card(slide2, Inches(5.0), Inches(4.45), Inches(7.733), Inches(2.38), "RAW TRANSACTIONAL DATA PREVIEW (ACTUAL MOVIES SAMPLE)")
raw_table_shape = slide2.shapes.add_table(5, 8, Inches(5.15), Inches(4.85), Inches(7.433), Inches(1.8))
rt = raw_table_shape.table
raw_col_widths = [Inches(1.8), Inches(0.7), Inches(0.7), Inches(0.8), Inches(0.9), Inches(0.7), Inches(0.7), Inches(1.133)]
for j, w in enumerate(raw_col_widths):
    rt.columns[j].width = w

raw_headers = ["Title", "Year", "Age", "IMDb", "Rotten Tom", "Netflix", "Prime", "Country"]
for j, h in enumerate(raw_headers):
    cell = rt.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = RGBColor(30, 41, 59)
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = "Arial"
    p.font.size = Pt(8)
    p.font.bold = True
    p.font.color.rgb = GOLD

raw_sample = [
    ("The Irishman", "2019", "18+", "7.8/10", "98/100", "1", "0", "United States"),
    ("Dangal", "2016", "7+", "8.4/10", "88/100", "1", "0", "India"),
    ("David Attenborough: Planet", "2020", "7+", "9.0/10", "95/100", "1", "0", "United Kingdom"),
    ("Lagaan: Once Upon a Time", "2001", "7+", "8.1/10", "94/100", "1", "0", "India, UK")
]

for i, row in enumerate(raw_sample):
    for j, val in enumerate(row):
        cell = rt.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(16, 26, 48) if i % 2 == 0 else RGBColor(22, 35, 64)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(7.5)
        p.font.color.rgb = TEXT_WHITE if j in (0, 4) else TEXT_BODY

print("Slide 2 generated.")

# ==============================================================================
# SLIDE 3: DATA CLEANING PROCESS
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
set_slide_background(slide3)
add_header_and_footer(slide3, 3, "DATA PREPROCESSING WORKFLOW, TEXT SANITIZATION & IMPUTATION")

# Top Visual Workflow Pipeline (6 Cards across width)
create_card(slide3, Inches(0.6), Inches(1.18), Inches(12.133), Inches(1.75), "END-TO-END DATA CLEANING & PREPARATION PIPELINE")

stages = [
    ("1. INGESTION", "Raw CSV Load", "9,515 raw records ingested via Pandas 2.2 engine"),
    ("2. SCHEMA AUDIT", "Missing Value Map", "Age: 4,177, IMDb: 206, Rotten Tomatoes: 7"),
    ("3. TEXT CLEANING", "String Sanitizing", "Stripped '/100' & '/10' suffix to parse float"),
    ("4. IMPUTATION", "Value Imputation", "Categorical modal mapping & target filtration"),
    ("5. ENGINEERING", "Feature Creation", "Rating category (High/Med/Low) & Exclusivity"),
    ("6. GOLD REPO", "Curated JSON/JS", "movies_data.js & cleaned_movies.json built")
]

step_w = Inches(1.9)
step_gap = Inches(0.12)
step_x = Inches(0.75)
step_y = Inches(1.58)

for idx, (num_title, subtitle, desc) in enumerate(stages):
    sx = step_x + idx * (step_w + step_gap)
    step_card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, sx, step_y, step_w, Inches(1.2))
    step_card.fill.solid()
    step_card.fill.fore_color.rgb = RGBColor(15, 23, 42)
    step_card.line.color.rgb = CYAN_TEXT if idx == 5 else SRU_BLUE
    step_card.line.width = Pt(1)

    stb = slide3.shapes.add_textbox(sx + Inches(0.08), step_y + Inches(0.08), step_w - Inches(0.16), Inches(1.04))
    stf = stb.text_frame
    stf.word_wrap = True
    sp1 = stf.paragraphs[0]
    sp1.text = num_title
    sp1.font.name = "Arial"
    sp1.font.size = Pt(8)
    sp1.font.bold = True
    sp1.font.color.rgb = GOLD if idx in (2, 4) else CYAN_TEXT

    sp2 = stf.add_paragraph()
    sp2.text = subtitle
    sp2.font.name = "Arial"
    sp2.font.size = Pt(8.5)
    sp2.font.bold = True
    sp2.font.color.rgb = TEXT_WHITE

    sp3 = stf.add_paragraph()
    sp3.text = desc
    sp3.font.name = "Arial"
    sp3.font.size = Pt(7.5)
    sp3.font.color.rgb = TEXT_MUTED

# Bottom 4 Deep-Dive Preprocessing Cards
prep_cards = [
    ("MISSING VALUE DETECTION", [
        ("Age Column", "4,177 Missing (43.9% of catalog)"),
        ("IMDb Column", "206 Missing (2.16% of catalog)"),
        ("Rotten Tomatoes", "7 Missing (0.07% - near complete)"),
        ("Country / Directors", "254 / 411 Missing respectively"),
        ("Status", "Identified in analyze_missing.py")
    ], Inches(0.6), Inches(3.08), Inches(2.9), Inches(3.75)),

    ("STRING PARSING & CASTING", [
        ("Rotten Tomatoes", "Stripped '/100' -> numeric float (98.0)"),
        ("IMDb Rating", "Stripped '/10' -> numeric float (7.8)"),
        ("Runtime Parsing", "Extracted numeric minutes float"),
        ("Type Conversion", "Year & Platform flags cast to int64"),
        ("Optimization", "Enables Seaborn statistical modeling")
    ], Inches(3.65), Inches(3.08), Inches(2.9), Inches(3.75)),

    ("IMPUTATION & LAB LOGIC", [
        ("replace_missing_values.py", "Script to impute missing values"),
        ("prepare_data.py", "Filters clean subset (5,338 titles)"),
        ("Age Categorization", "Mapped 'all', '7+', '13+', '16+', '18+'"),
        ("Rating Bins", "High (80-100), Med (60-79), Low (<60)"),
        ("Validation", "Handwritten Lab 3 checklist compliant")
    ], Inches(6.7), Inches(3.08), Inches(2.9), Inches(3.75)),

    ("FEATURE ENGINEERING & TECH", [
        ("Platform Count", "Sum of binary flags (Exclusivity Index)"),
        ("Multi-Country Unnesting", "Tokenized comma-separated countries"),
        ("JSON Serializer", "Exported cleaned_movies.json & data.js"),
        ("Python Libraries", "Pandas 2.2, NumPy 1.26, Seaborn 0.13"),
        ("Web Embedding", "Optimized offline array for Leaflet map")
    ], Inches(9.75), Inches(3.08), Inches(2.98), Inches(3.75))
]

for title, bullet_list, left, top, width, height in prep_cards:
    create_card(slide3, left, top, width, height, title)
    tb = slide3.shapes.add_textbox(left + Inches(0.15), top + Inches(0.45), width - Inches(0.3), height - Inches(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    for idx, (label, val) in enumerate(bullet_list):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = f"• {label}: "
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = CYAN_TEXT
        run = p.add_run()
        run.text = val
        run.font.name = "Arial"
        run.font.size = Pt(8)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY

print("Slide 3 generated.")

# ==============================================================================
# SLIDE 4: DATA ANALYSIS (EXECUTIVE BI SUMMARY)
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
set_slide_background(slide4)
add_header_and_footer(slide4, 4, "EXECUTIVE STREAMING ANALYTICS & STATISTICAL METRICS SUMMARY")

# Top 4 Giant Metric Cards
kpis = [
    ("TOTAL MOVIES ANALYZED", "9,515 Titles", "Across Netflix, Prime, Hulu, Disney+", CYAN_TEXT),
    ("PRIME VIDEO CATALOG", "4,113 Movies", "43.2% Global Catalog Share (Lead)", EMERALD),
    ("AVERAGE CRITIC RATING", "53.55 / 100", "Median: 52.0% | IMDb Mean: 6.16", GOLD),
    ("CONTENT EXCLUSIVITY RATE", "97.3% Exclusive", "9,262 Movies on Exactly 1 Platform", PURPLE)
]

card_w4 = Inches(2.88)
gap4 = Inches(0.2)
top4_x = Inches(0.6)
top4_y = Inches(1.18)

for idx, (kpi_title, kpi_val, kpi_sub, col) in enumerate(kpis):
    kx = top4_x + idx * (card_w4 + gap4)
    kc = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, kx, top4_y, card_w4, Inches(1.3))
    kc.fill.solid()
    kc.fill.fore_color.rgb = CARD_BG
    kc.line.color.rgb = col
    kc.line.width = Pt(1.5)

    ktb = slide4.shapes.add_textbox(kx + Inches(0.12), top4_y + Inches(0.1), card_w4 - Inches(0.24), Inches(1.1))
    ktf = ktb.text_frame
    ktf.word_wrap = True

    p0 = ktf.paragraphs[0]
    p0.text = kpi_title
    p0.font.name = "Arial"
    p0.font.size = Pt(8.5)
    p0.font.bold = True
    p0.font.color.rgb = TEXT_MUTED

    p1 = ktf.add_paragraph()
    p1.text = kpi_val
    p1.font.name = "Arial"
    p1.font.size = Pt(17)
    p1.font.bold = True
    p1.font.color.rgb = col

    p2 = ktf.add_paragraph()
    p2.text = kpi_sub
    p2.font.name = "Arial"
    p2.font.size = Pt(7.5)
    p2.font.color.rgb = TEXT_BODY

# Bottom 4 Analytical Dimensions
dim_cards = [
    ("PLATFORM CATALOG SHARE", [
        ("Prime Video (Lead)", "4,113 titles (43.2%) - Massive library"),
        ("Netflix (Rank 2)", "3,695 titles (38.8%) - Premium originals"),
        ("Hulu (Rank 3)", "1,047 titles (11.0%) - Curated TV/Film"),
        ("Disney+ (Specialized)", "922 titles (9.7%) - Family & franchise"),
        ("Catalog Overlap", "Only 253 titles shared across platforms"),
        ("Key Finding", "Prime Video & Netflix hold 82.0% of films")
    ], Inches(0.6), Inches(2.65), Inches(2.88), Inches(4.2)),

    ("AGE DEMOGRAPHIC SPLIT", [
        ("18+ Classification", "2,276 titles (42.6% of rated movies)"),
        ("7+ Classification", "1,090 titles (20.4% of rated movies)"),
        ("13+ Classification", "998 titles (18.7% of rated movies)"),
        ("all Classification", "698 titles (13.1% of rated movies)"),
        ("16+ Classification", "276 titles (5.2% of rated movies)"),
        ("Key Finding", "Mature (18+) is the largest single segment")
    ], Inches(3.68), Inches(2.65), Inches(2.88), Inches(4.2)),

    ("GEOGRAPHIC PRODUCTION HUBS", [
        ("United States (Lead)", "5,888 movie titles (61.9% share)"),
        ("United Kingdom", "960 movie titles (10.1% share)"),
        ("India (Bollywood/Reg)", "900 movie titles (9.5% share)"),
        ("Canada", "663 movie titles (7.0% share)"),
        ("France", "456 movie titles (4.8% share)"),
        ("Key Finding", "India is the 3rd largest content creator")
    ], Inches(6.76), Inches(2.65), Inches(2.88), Inches(4.2)),

    ("STATISTICAL & VIVA METRICS", [
        ("Mean Rotten Tomatoes", "53.55% | Median: 52.0% | Std: 13.20"),
        ("Mean IMDb Score", "6.16 / 10 | Median: 6.30 / 10"),
        ("Year vs RT Score", "Pearson r = -0.02 (Quality independent)"),
        ("Platform Exclusivity", "Negative correlation (r = -0.15 to -0.25)"),
        ("Seaborn Integration", "Boxplot, Violin, Histplot & Heatmap"),
        ("Key Finding", "Licensing exclusivity creates streaming moats")
    ], Inches(9.84), Inches(2.65), Inches(2.88), Inches(4.2))
]

for title, bullet_list, left, top, width, height in dim_cards:
    create_card(slide4, left, top, width, height, title)
    tb = slide4.shapes.add_textbox(left + Inches(0.12), top + Inches(0.42), width - Inches(0.24), height - Inches(0.5))
    tf = tb.text_frame
    tf.word_wrap = True
    for idx, (label, val) in enumerate(bullet_list):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = f"• {label}: "
        p.font.name = "Arial"
        p.font.size = Pt(8)
        p.font.bold = True
        p.font.color.rgb = CYAN_TEXT
        run = p.add_run()
        run.text = val
        run.font.name = "Arial"
        run.font.size = Pt(7.5)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY

print("Slide 4 generated.")

# ==============================================================================
# SLIDE 5: DATA VISUALIZATION: PLATFORM PERFORMANCE & RATINGS
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
set_slide_background(slide5)
add_header_and_footer(slide5, 5, "DATA VISUALIZATION: SEABORN DISTRIBUTIONS & RATING METRICS")

chart_col_w = Inches(3.88)
chart_gap = Inches(0.24)
start_cx = Inches(0.6)

# Chart 1: Boxplot
f1_path = os.path.join(FIG_DIR, "fig1_boxplot_age_ratings.png")
create_card(slide5, start_cx, Inches(1.18), chart_col_w, Inches(5.65), "FIG 1: BOXPLOT OF SCORES BY AGE")
if os.path.exists(f1_path):
    slide5.shapes.add_picture(f1_path, start_cx + Inches(0.1), Inches(1.55), width=chart_col_w - Inches(0.2), height=Inches(3.3))
tb1 = slide5.shapes.add_textbox(start_cx + Inches(0.12), Inches(4.95), chart_col_w - Inches(0.24), Inches(1.8))
tf1 = tb1.text_frame
tf1.word_wrap = True
p = tf1.paragraphs[0]
p.text = "Analytical Interpretation & Insights:"
p.font.name = "Arial"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = GOLD
p_body = tf1.add_paragraph()
p_body.text = "• 5-Number Summary: Depicts Min, Q1 (25%), Median (50%), Q3 (75%), and Max.\n• Median Rotten Tomatoes score across all age ratings hovers consistently between 50% and 54%.\n• Outliers (dots) reveal extreme critically acclaimed (>90%) or panned films."
p_body.font.name = "Arial"
p_body.font.size = Pt(7.8)
p_body.font.color.rgb = TEXT_BODY

# Chart 2: Violin Plot
f2_path = os.path.join(FIG_DIR, "fig2_violinplot_density.png")
cx2 = start_cx + chart_col_w + chart_gap
create_card(slide5, cx2, Inches(1.18), chart_col_w, Inches(5.65), "FIG 2: VIOLIN PLOT - SCORE DENSITY")
if os.path.exists(f2_path):
    slide5.shapes.add_picture(f2_path, cx2 + Inches(0.1), Inches(1.55), width=chart_col_w - Inches(0.2), height=Inches(3.3))
tb2 = slide5.shapes.add_textbox(cx2 + Inches(0.12), Inches(4.95), chart_col_w - Inches(0.24), Inches(1.8))
tf2 = tb2.text_frame
tf2.word_wrap = True
p = tf2.paragraphs[0]
p.text = "Analytical Interpretation & Insights:"
p.font.name = "Arial"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = GOLD
p_body = tf2.add_paragraph()
p_body.text = "• Combines a mini boxplot with Kernel Density Estimation (KDE) on both sides.\n• Noticeable 'bulge' in the center around 40-55% across all age categories.\n• Confirms the vast majority of catalog titles are average, with thin tails extending to 100%."
p_body.font.name = "Arial"
p_body.font.size = Pt(7.8)
p_body.font.color.rgb = TEXT_BODY

# Chart 3: Histogram + KDE
f3_path = os.path.join(FIG_DIR, "fig3_histplot_kde.png")
cx3 = start_cx + (chart_col_w + chart_gap) * 2
create_card(slide5, cx3, Inches(1.18), chart_col_w, Inches(5.65), "FIG 3: HISTOGRAM WITH KDE CURVE")
if os.path.exists(f3_path):
    slide5.shapes.add_picture(f3_path, cx3 + Inches(0.1), Inches(1.55), width=chart_col_w - Inches(0.2), height=Inches(3.3))
tb3 = slide5.shapes.add_textbox(cx3 + Inches(0.12), Inches(4.95), chart_col_w - Inches(0.24), Inches(1.8))
tf3 = tb3.text_frame
tf3.word_wrap = True
p = tf3.paragraphs[0]
p.text = "Analytical Interpretation & Insights:"
p.font.name = "Arial"
p.font.size = Pt(8.5)
p.font.bold = True
p.font.color.rgb = GOLD
p_body = tf3.add_paragraph()
p_body.text = "• Univariate continuous distribution across 25 bins with smooth KDE overlay.\n• Empirical distribution approximates a Gaussian curve centered at Mean 53.55%.\n• Demonstrates objective, unskewed critic assessment distribution across streaming media."
p_body.font.name = "Arial"
p_body.font.size = Pt(7.8)
p_body.font.color.rgb = TEXT_BODY

print("Slide 5 generated.")

# ==============================================================================
# SLIDE 6: PLOTS AND CONCLUSIONS
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
set_slide_background(slide6)
add_header_and_footer(slide6, 6, "DEEP-DIVE HEATMAP, CATALOG SHARES & STRATEGIC INDUSTRY CONCLUSIONS")

f4_path = os.path.join(FIG_DIR, "fig4_correlation_heatmap.png")
f5_path = os.path.join(FIG_DIR, "fig5_platform_catalog_share.png")
f6_path = os.path.join(FIG_DIR, "fig6_country_exclusivity.png")

col_w6 = Inches(3.88)
gap6 = Inches(0.24)
y6_top = Inches(1.18)
h6_top = Inches(3.2)

# Fig 4: Heatmap
create_card(slide6, start_cx, y6_top, col_w6, h6_top, "FIG 4: SEABORN CORRELATION HEATMAP")
if os.path.exists(f4_path):
    slide6.shapes.add_picture(f4_path, start_cx + Inches(0.1), y6_top + Inches(0.38), width=col_w6 - Inches(0.2), height=h6_top - Inches(0.48))

# Fig 5: Platform Catalog Share
cx5 = start_cx + col_w6 + gap6
create_card(slide6, cx5, y6_top, col_w6, h6_top, "FIG 5: PLATFORM CATALOG & MARKET SHARE")
if os.path.exists(f5_path):
    slide6.shapes.add_picture(f5_path, cx5 + Inches(0.1), y6_top + Inches(0.38), width=col_w6 - Inches(0.2), height=h6_top - Inches(0.48))

# Fig 6: Country & Exclusivity
cx6 = start_cx + (col_w6 + gap6) * 2
create_card(slide6, cx6, y6_top, col_w6, h6_top, "FIG 6: ORIGIN & CONTENT EXCLUSIVITY")
if os.path.exists(f6_path):
    slide6.shapes.add_picture(f6_path, cx6 + Inches(0.1), y6_top + Inches(0.38), width=col_w6 - Inches(0.2), height=h6_top - Inches(0.48))

# Bottom Row: 4 Strategic Conclusions
y6_bot = Inches(4.5)
h6_bot = Inches(2.35)
card_w6b = Inches(2.88)
gap6b = Inches(0.2)

conclusions = [
    ("1. EXCLUSIVITY AS STREAMING MOAT",
     "97.3% of all movie titles (9,262 films) are exclusive to a single platform.\n"
     "Conclusion: Streaming services compete strictly through proprietary licensing barriers rather than shared broad catalogs.",
     CYAN_TEXT),
    ("2. VOLUME VS. ORIGINAL PRODUCTION",
     "Prime Video leads global volume (4,113 titles / 43.2%), while Netflix emphasizes high-budget proprietary productions (3,695 titles).\n"
     "Conclusion: Prime focuses on back-catalog depth; Netflix focuses on cultural zeitgeist.",
     GOLD),
    ("3. DEMOGRAPHIC SPECIALIZATION",
     "Mature 18+ content accounts for 42.6% of rated titles, while Disney+ dominates the 'all' and '7+' family segment (922 curated titles).\n"
     "Conclusion: OTT platforms exhibit deliberate audience demographic segmentation.",
     EMERALD),
    ("4. GLOBAL EXPANSION IN INDIA & UK",
     "India (900 titles) and the United Kingdom (960 titles) represent the largest production hubs outside the United States.\n"
     "Conclusion: Regional language localization and Bollywood acquisitions are essential for subscriber retention in Asia.",
     PURPLE)
]

for idx, (title_c, text_c, col_c) in enumerate(conclusions):
    bx = start_cx + idx * (card_w6b + gap6b)
    c_box = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, y6_bot, card_w6b, h6_bot)
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = CARD_BG
    c_box.line.color.rgb = col_c
    c_box.line.width = Pt(1.2)

    ctb = slide6.shapes.add_textbox(bx + Inches(0.1), y6_bot + Inches(0.1), card_w6b - Inches(0.2), h6_bot - Inches(0.2))
    ctf = ctb.text_frame
    ctf.word_wrap = True

    p0 = ctf.paragraphs[0]
    p0.text = title_c
    p0.font.name = "Arial"
    p0.font.size = Pt(8.5)
    p0.font.bold = True
    p0.font.color.rgb = col_c

    p1 = ctf.add_paragraph()
    p1.text = text_c
    p1.font.name = "Arial"
    p1.font.size = Pt(7.5)
    p1.font.color.rgb = TEXT_BODY

print("Slide 6 generated.")

# ==============================================================================
# SLIDE 7: FINAL INTERACTIVE DASHBOARD
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
set_slide_background(slide7)
add_header_and_footer(slide7, 7, "FINAL INTERACTIVE DASHBOARD SHOWCASE & COUNTRY RECALCULATION")

# Left: Main Dashboard Screenshot
dash_main_path = os.path.join(BASE_DIR, "screenshot.png")
create_card(slide7, Inches(0.6), Inches(1.18), Inches(7.9), Inches(5.65), "FIG 7A: STREAMING PLATFORMS INTERACTIVE DASHBOARD (OVERVIEW)")
if os.path.exists(dash_main_path):
    slide7.shapes.add_picture(dash_main_path, Inches(0.72), Inches(1.58), width=Inches(7.66), height=Inches(4.6))

cap_tb = slide7.shapes.add_textbox(Inches(0.72), Inches(6.25), Inches(7.66), Inches(0.5))
ctf = cap_tb.text_frame
ctf.word_wrap = True
cp = ctf.paragraphs[0]
cp.text = "Production Interactive Streaming Dashboard: Integrated with Google Earth-style Esri satellite map, KPI metric tags, dynamic country filters, and real-time demographic recalculations."
cp.font.name = "Arial"
cp.font.size = Pt(8)
cp.font.color.rgb = TEXT_MUTED

# Right Top: Filtered View Screenshot (India)
dash_filt_path = os.path.join(BASE_DIR, "screenshot_dashboard_india.png")
create_card(slide7, Inches(8.65), Inches(1.18), Inches(4.08), Inches(3.1), "FIG 7B: DYNAMIC FILTER (INDIA SELECTED)")
if os.path.exists(dash_filt_path):
    slide7.shapes.add_picture(dash_filt_path, Inches(8.75), Inches(1.52), width=Inches(3.88), height=Inches(2.45))

# Right Bottom: Interactive Capabilities Callout
create_card(slide7, Inches(8.65), Inches(4.4), Inches(4.08), Inches(2.43), "CORE DASHBOARD CAPABILITIES")
ic_tb = slide7.shapes.add_textbox(Inches(8.75), Inches(4.75), Inches(3.88), Inches(1.95))
itf = ic_tb.text_frame
itf.word_wrap = True

features = [
    ("Global Country Filtering", "Clicking any country instantly recalculates title count, platform share, and ratings."),
    ("Multi-Layer Satellite Map", "Esri World Imagery, CartoDB streets, and topographic terrain switching."),
    ("Dynamic Platform Slicers", "Interactive toggles for Netflix, Hulu, Prime Video, and Disney+."),
    ("Zero-Latency Offline Architecture", "Embedded GeoJSON boundaries & movies_data.js for high-speed client rendering.")
]

for idx, (head, text_f) in enumerate(features):
    p = itf.paragraphs[0] if idx == 0 else itf.add_paragraph()
    p.text = f"• {head}: "
    p.font.name = "Arial"
    p.font.size = Pt(8)
    p.font.bold = True
    p.font.color.rgb = CYAN_TEXT
    run = p.add_run()
    run.text = text_f
    run.font.name = "Arial"
    run.font.size = Pt(7.5)
    run.font.color.rgb = TEXT_BODY

print("Slide 7 generated.")

# ==============================================================================
# SLIDE 8: PROJECT ARCHITECTURE AND MAP DESIGN (LEAD: VED PRAKASH)
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
set_slide_background(slide8)
add_header_and_footer(slide8, 8, "PROJECT ARCHITECTURE & REALISTIC SATELLITE MAP (LEAD: VED PRAKASH)")

# Left: System Architecture Flow (Width ~5.4 in)
create_card(slide8, Inches(0.6), Inches(1.18), Inches(5.4), Inches(5.65), "END-TO-END SYSTEM ARCHITECTURE & STACK")

arch_steps = [
    ("DATA INGESTION LAYER", "9,515 Movies CSV Engine", "Ingests raw streaming catalogs, parses 17 schema fields and metadata.", SRU_BLUE),
    ("PREPROCESSING & IMPUTATION", "Pandas / NumPy / Python", "Cleans Rotten Tomatoes text, handles missing Age ratings, builds JSON data.", CYAN_TEXT),
    ("STATISTICAL & EDA ENGINE", "Seaborn 0.13 / Matplotlib", "Computes boxplots, violin plots, KDE distributions, and correlation matrices.", EMERALD),
    ("GEOSPATIAL SATELLITE ENGINE", "Leaflet JS / Esri Imagery", "Sub-meter photorealistic satellite tiles, stable 2D top-down view, HUD.", GOLD),
    ("INTERACTIVE DASHBOARD LAYER", "HTML5 / Tailwind / Chart.js", "Reactive dashboard UI, dynamic country click filtering, iframe sync.", PURPLE),
    ("DOCUMENTATION & REPORTS", "DAV Project Report (.docx)", "8-chapter university report, lab viva notes, automated test suites.", SRU_NAVY)
]

step_h = Inches(0.68)
step_gap8 = Inches(0.1)
y_arch = Inches(1.58)

for idx, (tier_title, tech, desc, tcol) in enumerate(arch_steps):
    sy = y_arch + idx * (step_h + step_gap8)
    sc = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.78), sy, Inches(5.04), step_h)
    sc.fill.solid()
    sc.fill.fore_color.rgb = RGBColor(16, 26, 48)
    sc.line.color.rgb = tcol
    sc.line.width = Pt(1)

    stb = slide8.shapes.add_textbox(Inches(0.88), sy + Inches(0.04), Inches(4.84), step_h - Inches(0.08))
    stf = stb.text_frame
    stf.word_wrap = True
    sp1 = stf.paragraphs[0]
    sp1.text = f"{tier_title} [{tech}]"
    sp1.font.name = "Arial"
    sp1.font.size = Pt(8)
    sp1.font.bold = True
    sp1.font.color.rgb = tcol

    sp2 = stf.add_paragraph()
    sp2.text = desc
    sp2.font.name = "Arial"
    sp2.font.size = Pt(7.5)
    sp2.font.color.rgb = TEXT_BODY

tech_box = slide8.shapes.add_textbox(Inches(0.78), Inches(6.25), Inches(5.04), Inches(0.45))
ttf = tech_box.text_frame
ttf.word_wrap = True
tp = ttf.paragraphs[0]
tp.text = "Technology Stack: Python 3.14 | Pandas | NumPy | Seaborn | Matplotlib | Leaflet.js | Esri GIS | Tailwind CSS"
tp.font.name = "Arial"
tp.font.size = Pt(7.5)
tp.font.bold = True
tp.font.color.rgb = CYAN_TEXT

# Right: Dedicated Realistic Satellite Map Design Section (Lead: Ved Prakash)
map_path = os.path.join(FIG_DIR, "satellite_map_lead_ved.png")
c_map = create_card(slide8, Inches(6.2), Inches(1.18), Inches(6.533), Inches(5.65), "REALISTIC GOOGLE EARTH-STYLE SATELLITE WORLD MAP")

# Prominent Attribution Banner for Ved Prakash
attr_card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.35), Inches(1.55), Inches(6.233), Inches(0.52))
attr_card.fill.solid()
attr_card.fill.fore_color.rgb = RGBColor(28, 40, 75)
attr_card.line.color.rgb = GOLD
attr_card.line.width = Pt(1.5)
ab_tf = attr_card.text_frame
ab_tf.word_wrap = True
ab_p = ab_tf.paragraphs[0]
ab_p.alignment = PP_ALIGN.CENTER
ab_p.text = "GEOGRAPHICAL SATELLITE MAP DESIGNED & INTEGRATED BY: VED PRAKASH (2503A520Q2)"
ab_p.font.name = "Arial"
ab_p.font.size = Pt(9)
ab_p.font.bold = True
ab_p.font.color.rgb = GOLD

# Map Screenshot
if os.path.exists(map_path):
    slide8.shapes.add_picture(map_path, Inches(6.35), Inches(2.18), width=Inches(6.233), height=Inches(3.3))

# Map Architecture Callout
map_tb = slide8.shapes.add_textbox(Inches(6.35), Inches(5.55), Inches(6.233), Inches(1.15))
mtf = map_tb.text_frame
mtf.word_wrap = True
mp1 = mtf.paragraphs[0]
mp1.text = "Satellite Mapping Engine Specifications (Ved Prakash):"
mp1.font.name = "Arial"
mp1.font.size = Pt(8.5)
mp1.font.bold = True
mp1.font.color.rgb = CYAN_TEXT

mp2 = mtf.add_paragraph()
mp2.text = "• Esri World Imagery (ArcGIS) tiles: Sub-meter photorealistic imagery up to zoom level 20 (reveals terrain, roads, building footprints).\n• Stable 2D Top-Down View: Fixed North perspective with zero auto-rotation, zero auto-spin, and smooth inertial panning.\n• Multi-Layer Controls: Hybrid Satellite, Pure Satellite, Street Map, and Topographic Terrain with Nominatim Instant Search."
mp2.font.name = "Arial"
mp2.font.size = Pt(7.5)
mp2.font.color.rgb = TEXT_BODY

print("Slide 8 generated.")

# ==============================================================================
# SLIDE 9: ACADEMIC PROJECT REPORT AND DOCUMENTATION
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
set_slide_background(slide9)
add_header_and_footer(slide9, 9, "ACADEMIC DOCUMENTATION & 8-CHAPTER UNIVERSITY REPORT ALIGNMENT")

# Left: Report Screenshots
rep_path = os.path.join(BASE_DIR, "report_screenshot.png")
create_card(slide9, Inches(0.6), Inches(1.18), Inches(5.2), Inches(5.65), "AUTHENTIC REPORT & LAB ARTIFACTS")

if os.path.exists(rep_path):
    slide9.shapes.add_picture(rep_path, Inches(0.8), Inches(1.6), width=Inches(4.8), height=Inches(3.1))

# Caption for report screenshots
rtb = slide9.shapes.add_textbox(Inches(0.8), Inches(4.85), Inches(4.8), Inches(1.85))
rtf = rtb.text_frame
rtf.word_wrap = True
rp1 = rtf.paragraphs[0]
rp1.text = "Official Academic Documentation & Lab Artifacts:"
rp1.font.name = "Arial"
rp1.font.size = Pt(8.5)
rp1.font.bold = True
rp1.font.color.rgb = GOLD

rp2 = rtf.add_paragraph()
rp2.text = "• Formatted strictly in accordance with SR University CSAI guidelines.\n• Includes handwritten notes (Lab_Assignment_3_Handwritten_Notes.pdf), comprehensive project notes (dav project notes.pdf), viva revision cheat-sheets, and automated Puppeteer test suites (test_satellite_map.js, verify_dashboard.js)."
rp2.font.name = "Arial"
rp2.font.size = Pt(7.5)
rp2.font.color.rgb = TEXT_BODY

# Right: 8 Chapters Breakdown Card
create_card(slide9, Inches(6.0), Inches(1.18), Inches(6.733), Inches(5.65), "UNIVERSITY REPORT CHAPTER-BY-CHAPTER COMPLIANCE")

chapters = [
    ("Chapter 1", "Introduction, Problem Statement & OTT Landscape", "Streaming platform growth, catalog discovery problem, objectives"),
    ("Chapter 2", "Dataset Architecture, Provenance & Ingestion", "Kaggle dataset origin, 17 attributes, 9,515 titles, data schema"),
    ("Chapter 3", "Exploratory Data Analysis, Missing Values & ETL", "Text sanitization of Rotten Tomatoes, Age imputation, cleaning scripts"),
    ("Chapter 4", "Realistic Satellite World Map Integration", "Lead: Ved Prakash – Esri sub-meter tiles, Leaflet GIS, stable 2D controls"),
    ("Chapter 5", "Interactive Dashboard Architecture & Deployment", "Lead: Darshan Kumar – Reactive dashboard UI, dynamic country filters"),
    ("Chapter 6", "Empirical Findings, Statistical Analysis & Viva Q/A", "Boxplots, violins, KDE curves, Pearson correlation, viva solutions"),
    ("Chapter 7", "System Limitations & Future Enhancements", "Live streaming API telemetry, personalized ML recommendation engine"),
    ("Chapter 8", "Conclusion, Deliverables & Academic References", "Summary of contributions, GitHub repo, and formal IEEE citations")
]

ch_table_shape = slide9.shapes.add_table(9, 3, Inches(6.15), Inches(1.58), Inches(6.433), Inches(4.2))
cht = ch_table_shape.table
cht.columns[0].width = Inches(1.1)
cht.columns[1].width = Inches(2.6)
cht.columns[2].width = Inches(2.733)

ch_headers = ["Chapter", "Formal Chapter Title", "Detailed Content & Academic Coverage"]
for j, h in enumerate(ch_headers):
    cell = cht.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = SRU_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = "Arial"
    p.font.size = Pt(8)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

for i, (chn, chtit, chcov) in enumerate(chapters):
    for j, val in enumerate([chn, chtit, chcov]):
        cell = cht.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(16, 26, 48) if i % 2 == 0 else RGBColor(22, 35, 64)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(7.5)
        p.font.color.rgb = GOLD if (j == 0 and i in (3, 4)) else (TEXT_WHITE if j == 0 else (CYAN_TEXT if j == 1 else TEXT_BODY))

repo_tb = slide9.shapes.add_textbox(Inches(6.15), Inches(5.9), Inches(6.433), Inches(0.8))
r_tf = repo_tb.text_frame
r_tf.word_wrap = True
r_p = r_tf.paragraphs[0]
r_p.text = "Project Artifacts & Links: GitHub (@gyan0099) | Live Dashboard (dashboard.html) | Word Report (.docx) | Presentation (.pptx & .pdf)"
r_p.font.name = "Arial"
r_p.font.size = Pt(8)
r_p.font.bold = True
r_p.font.color.rgb = CYAN_TEXT

print("Slide 9 generated.")

# ==============================================================================
# SLIDE 10: TEAM CONTRIBUTIONS, CONCLUSION & CLOSING
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
set_slide_background(slide10)
add_header_and_footer(slide10, 10, "TEAM RESPONSIBILITY MATRIX, PROJECT CONCLUSION & ACKNOWLEDGMENTS")

# Left: 3 Comprehensive Team Contribution Cards
create_card(slide10, Inches(0.6), Inches(1.18), Inches(7.7), Inches(5.65), "INDIVIDUAL TEAM CONTRIBUTIONS & RESPONSIBILITY MATRIX")

team_details = [
    ("VED PRAKASH", "2503A520Q2", "GEOSPATIAL SATELLITE MAP LEAD",
     [
         ("Realistic Satellite Engine", "Integrated Esri World Imagery (ArcGIS) sub-meter tiles into dashboard.html with zoom level 20."),
         ("Map Stability & Controls", "Engineered stable 2D top-down view (zero auto-rotation/auto-spin), full-screen toggle, & coordinate HUD."),
         ("Deck Synthesis", "Spearheaded the 10-slide academic PowerPoint presentation, data visualization layout, and theme architecture."),
         ("Report Authoring", "Authored Chapter 4 (Geospatial Satellite Integration) and Chapter 5 (Interactive Dashboard Architecture).")
     ], CARD_BG, CARD_BORDER),

    ("DARSHAN KUMAR", "2503A520P9", "GROUP LEADER & SYSTEM ARCHITECT",
     [
         ("Project Leadership", "Coordinated team milestones, task allocation, code repository integration, and academic reviews."),
         ("Dashboard Architecture", "Designed reactive country-filter recalculation engine, multi-platform slicers, and summary cards."),
         ("Statistical Modeling", "Executed Pearson correlation matrix, content exclusivity modeling, and streaming retail conclusions."),
         ("Report Authoring", "Authored Chapter 1 (Introduction), Chapter 6 (Empirical Findings & Viva Q/A), and Chapter 8 (Conclusion).")
     ], RGBColor(28, 40, 75), GOLD),

    ("SASHWAT GHOSH", "2503A52588", "DATA CLEANING & EDA LEAD",
     [
         ("ETL & Text Sanitization", "Engineered prepare_data.py to strip '/100' string suffixes from Rotten Tomatoes into clean numeric floats."),
         ("Missing Value Imputation", "Developed replace_missing_values.py to analyze and impute 4,177 unrated Age demographic entries."),
         ("Seaborn Visualization", "Implemented boxplot, violin plot, and histogram KDE charts matching Lab Assignment 3 specifications."),
         ("Report Authoring", "Authored Chapter 2 (Dataset Description) and Chapter 3 (Exploratory Data Analysis).")
     ], CARD_BG, CARD_BORDER)
]

y_team = Inches(1.58)
h_team = Inches(1.6)
g_team = Inches(0.12)

for idx, (tname, troll, trole, task_list, tbg, tbdr) in enumerate(team_details):
    cy = y_team + idx * (h_team + g_team)
    tc_shape = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.78), cy, Inches(7.34), h_team)
    tc_shape.fill.solid()
    tc_shape.fill.fore_color.rgb = tbg
    tc_shape.line.color.rgb = tbdr
    tc_shape.line.width = Pt(1.5 if tbdr == GOLD else 1)

    ttb = slide10.shapes.add_textbox(Inches(0.9), cy + Inches(0.06), Inches(7.1), h_team - Inches(0.12))
    ttf = ttb.text_frame
    ttf.word_wrap = True

    p0 = ttf.paragraphs[0]
    p0.text = f"{tname}  |  Roll No: {troll}  •  {trole}"
    p0.font.name = "Arial"
    p0.font.size = Pt(9.5)
    p0.font.bold = True
    p0.font.color.rgb = GOLD if tbdr == GOLD else CYAN_TEXT

    for task_name, task_desc in task_list:
        p_task = ttf.add_paragraph()
        p_task.text = f"• {task_name}: "
        p_task.font.name = "Arial"
        p_task.font.size = Pt(7.5)
        p_task.font.bold = True
        p_task.font.color.rgb = TEXT_WHITE
        run = p_task.add_run()
        run.text = task_desc
        run.font.name = "Arial"
        run.font.size = Pt(7.5)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY

# Right: Conclusion & Professional Closing (Width ~4.2 in)
create_card(slide10, Inches(8.5), Inches(1.18), Inches(4.233), Inches(2.75), "EXECUTIVE PROJECT CONCLUSION")
conc_tb = slide10.shapes.add_textbox(Inches(8.65), Inches(1.55), Inches(3.933), Inches(2.25))
ctf = conc_tb.text_frame
ctf.word_wrap = True

p_c1 = ctf.paragraphs[0]
p_c1.text = "Summary of Academic & Technical Impact:"
p_c1.font.name = "Arial"
p_c1.font.size = Pt(8.5)
p_c1.font.bold = True
p_c1.font.color.rgb = GOLD

p_c2 = ctf.add_paragraph()
p_c2.text = "1. Technical Mastery: Delivered full-stack data analytics from 9,515 raw film records to an interactive Google Earth-style satellite map.\n2. Statistical Rigor: Applied Seaborn boxplots, violin plots, KDE distributions, and correlation heatmaps strictly fulfilling Lab 3.\n3. Business Relevance: Uncovered key OTT dynamics (97.3% catalog exclusivity, Prime Video volume lead, and India's production surge)."
p_c2.font.name = "Arial"
p_c2.font.size = Pt(7.5)
p_c2.font.color.rgb = TEXT_BODY

# Thank You / Q&A Card
create_card(slide10, Inches(8.5), Inches(4.08), Inches(4.233), Inches(2.75), "THANK YOU & Q/A INVITATION")
ty_tb = slide10.shapes.add_textbox(Inches(8.65), Inches(4.45), Inches(3.933), Inches(2.25))
tytf = ty_tb.text_frame
tytf.word_wrap = True

tp1 = tytf.paragraphs[0]
tp1.text = "THANK YOU!"
tp1.font.name = "Arial"
tp1.font.size = Pt(18)
tp1.font.bold = True
tp1.font.color.rgb = TEXT_WHITE

tp2 = tytf.add_paragraph()
tp2.text = "We welcome questions, evaluations, and guidance from our faculty and evaluators."
tp2.font.name = "Arial"
tp2.font.size = Pt(8.5)
tp2.font.color.rgb = TEXT_BODY

tp3 = tytf.add_paragraph()
tp3.text = "\nSR UNIVERSITY, WARANGAL\nSchool of Computer Science & Artificial Intelligence\nCourse: Data Analytics & Visualization (25CAI202PC201)\nAcademic Year: 2026–27"
tp3.font.name = "Arial"
tp3.font.size = Pt(8)
tp3.font.bold = True
tp3.font.color.rgb = CYAN_TEXT

print("Slide 10 generated.")

# Save presentation to Dav project directory and Desktop
output_paths = [
    os.path.join(BASE_DIR, "Streaming_Platforms_Dashboard_Presentation.pptx"),
    os.path.join(BASE_DIR, "GYAN_DAV_LAB_PROJECT_1.pptx"),
    "/Users/vedprakash/Desktop/Streaming_Platforms_Dashboard_Presentation.pptx",
    "/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1.pptx",
    "/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1/Streaming_Platforms_Dashboard_Presentation.pptx",
    "/Users/vedprakash/Desktop/GYAN_DAV_LAB_PROJECT_1/GYAN_DAV_LAB_PROJECT_1.pptx"
]

for p in output_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    prs.save(p)
    print(f"Saved: {p} (Size: {os.path.getsize(p):,} bytes)")

print("All 10 slides successfully built and saved for Streaming Platforms Dashboard!")
