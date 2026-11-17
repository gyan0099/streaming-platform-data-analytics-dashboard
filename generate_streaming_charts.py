import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = "/Users/vedprakash/Desktop/Dav project"
OUT_DIR = os.path.join(BASE_DIR, "presentation_figures")
os.makedirs(OUT_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(BASE_DIR, "MoviesOnStreamingPlatforms (4).csv"))

# Data cleaning
df['RT_clean'] = df['Rotten Tomatoes'].astype(str).str.replace('/100', '').str.replace('%', '').str.strip()
df['Rotten Tomatoes'] = pd.to_numeric(df['RT_clean'], errors='coerce')
df['IMDb_clean'] = df['IMDb'].astype(str).str.replace('/10', '').str.strip()
df['IMDb'] = pd.to_numeric(df['IMDb_clean'], errors='coerce')

# Filter for Age rating analyses
age_order = ['all', '7+', '13+', '16+', '18+']
plot_df = df[df['Age'].isin(age_order) & df['Rotten Tomatoes'].notnull()].copy()

# Palette from lab assignment notes
palette = {
    'all': '#2ecc71',  # Green
    '7+':  '#3498db',  # Blue
    '13+': '#f1c40f',  # Yellow
    '16+': '#e67e22',  # Orange
    '18+': '#e74c3c'   # Red
}

# Dark theme configuration for publication presentation
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.facecolor'] = '#0B132B'
plt.rcParams['axes.facecolor'] = '#141F38'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.labelcolor'] = '#E2E8F0'
plt.rcParams['xtick.color'] = '#94A3B8'
plt.rcParams['ytick.color'] = '#94A3B8'
plt.rcParams['text.color'] = '#F8FAFC'
plt.rcParams['grid.color'] = '#1E293B'

# -------------------------------------------------------------
# 1. Boxplot: Rotten Tomatoes Distribution by Age Rating
# -------------------------------------------------------------
plt.figure(figsize=(7, 4.5), dpi=300)
ax = sns.boxplot(
    data=plot_df,
    x='Age',
    y='Rotten Tomatoes',
    order=age_order,
    palette=palette,
    width=0.55,
    linewidth=1.4,
    fliersize=3.5,
    flierprops=dict(marker='o', color='#38BDF8', alpha=0.6)
)
plt.title('Figure 1: Rotten Tomatoes Score Distribution by Age Rating', fontsize=12, fontweight='bold', pad=12, color='#FFFFFF')
plt.xlabel('Age Rating Classification', fontsize=10, fontweight='bold', labelpad=8)
plt.ylabel('Rotten Tomatoes Score (%)', fontsize=10, fontweight='bold', labelpad=8)
plt.grid(axis='y', linestyle='--', alpha=0.3)
# Annotate medians
for i, age in enumerate(age_order):
    med = plot_df[plot_df['Age'] == age]['Rotten Tomatoes'].median()
    ax.text(i, med + 1.8, f'{med:.0f}%', horizontalalignment='center', size=9, color='#FFFFFF', weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig1_boxplot_age_ratings.png"), dpi=300)
plt.close()
print("Saved fig1_boxplot_age_ratings.png")

# -------------------------------------------------------------
# 2. Violinplot: Probability Density by Age Rating
# -------------------------------------------------------------
plt.figure(figsize=(7, 4.5), dpi=300)
ax = sns.violinplot(
    data=plot_df,
    x='Age',
    y='Rotten Tomatoes',
    order=age_order,
    palette=palette,
    width=0.7,
    linewidth=1.2,
    inner='quartile'
)
plt.title('Figure 2: Violin Plot - Score Density & Spread by Age Group', fontsize=12, fontweight='bold', pad=12, color='#FFFFFF')
plt.xlabel('Age Rating Classification', fontsize=10, fontweight='bold', labelpad=8)
plt.ylabel('Rotten Tomatoes Score (%)', fontsize=10, fontweight='bold', labelpad=8)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig2_violinplot_density.png"), dpi=300)
plt.close()
print("Saved fig2_violinplot_density.png")

# -------------------------------------------------------------
# 3. Histogram with KDE Curve (Target Distribution)
# -------------------------------------------------------------
plt.figure(figsize=(7, 4.5), dpi=300)
sns.histplot(
    data=plot_df,
    x='Rotten Tomatoes',
    kde=True,
    bins=25,
    color='#38BDF8',
    edgecolor='#0B132B',
    line_kws={'linewidth': 2.5, 'color': '#F59E0B'}
)
plt.title('Figure 3: Univariate Catalog Rating Distribution (Hist + KDE)', fontsize=12, fontweight='bold', pad=12, color='#FFFFFF')
plt.xlabel('Rotten Tomatoes Score (%)', fontsize=10, fontweight='bold', labelpad=8)
plt.ylabel('Movie Count', fontsize=10, fontweight='bold', labelpad=8)
mean_rt = plot_df['Rotten Tomatoes'].mean()
median_rt = plot_df['Rotten Tomatoes'].median()
plt.axvline(mean_rt, color='#EF4444', linestyle='--', linewidth=1.5, label=f'Mean: {mean_rt:.1f}%')
plt.axvline(median_rt, color='#10B981', linestyle='-', linewidth=1.5, label=f'Median: {median_rt:.1f}%')
plt.legend(frameon=True, facecolor='#141F38', edgecolor='#334155', fontsize=9)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig3_histplot_kde.png"), dpi=300)
plt.close()
print("Saved fig3_histplot_kde.png")

# -------------------------------------------------------------
# 4. Correlation Heatmap (Seaborn coolwarm)
# -------------------------------------------------------------
nums_cols = ['Year', 'Rotten Tomatoes', 'Netflix', 'Hulu', 'Prime Video', 'Disney+']
corr = plot_df[nums_cols].corr()

plt.figure(figsize=(6.5, 5), dpi=300)
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    fmt=".2f",
    square=True,
    linewidths=1,
    linecolor='#0B132B',
    cbar_kws={'label': 'Pearson Correlation (r)'}
)
plt.title('Figure 4: Correlation Matrix (Year, Ratings, Platforms)', fontsize=12, fontweight='bold', pad=12, color='#FFFFFF')
plt.xticks(rotation=30, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig4_correlation_heatmap.png"), dpi=300)
plt.close()
print("Saved fig4_correlation_heatmap.png")

# -------------------------------------------------------------
# 5. Platform Catalog Volume & Market Share
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), dpi=300, facecolor='#0B132B')
platforms = ['Prime Video', 'Netflix', 'Hulu', 'Disney+']
counts = [df['Prime Video'].sum(), df['Netflix'].sum(), df['Hulu'].sum(), df['Disney+'].sum()]
colors = ['#00A8E1', '#E50914', '#1CE783', '#113CCF']

# Bar chart
bars = ax1.bar(platforms, counts, color=colors, width=0.6, edgecolor='#FFFFFF', linewidth=0.5)
ax1.set_facecolor('#141F38')
ax1.set_title('Movie Catalog Volume by Platform', fontsize=10, fontweight='bold', color='#FFFFFF', pad=10)
ax1.set_ylabel('Number of Movies', fontsize=9, color='#E2E8F0')
ax1.grid(axis='y', linestyle='--', alpha=0.3)
ax1.tick_params(axis='x', rotation=25, labelsize=8)
for b in bars:
    h = b.get_height()
    ax1.text(b.get_x() + b.get_width()/2, h + 80, f'{h:,}', ha='center', va='bottom', fontsize=8, color='#FFFFFF', weight='bold')

# Donut chart
wedges, texts, autotexts = ax2.pie(
    counts,
    labels=platforms,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.75,
    textprops=dict(color='#FFFFFF', fontsize=8),
    wedgeprops=dict(width=0.45, edgecolor='#0B132B', linewidth=2)
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_weight('bold')
ax2.set_title('Platform Catalog Market Share', fontsize=10, fontweight='bold', color='#FFFFFF', pad=10)

plt.suptitle('Figure 5: Streaming Platform Catalog Size & Market Distribution', fontsize=11, fontweight='bold', color='#38BDF8', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig5_platform_catalog_share.png"), dpi=300)
plt.close()
print("Saved fig5_platform_catalog_share.png")

# -------------------------------------------------------------
# 6. Top Content Producing Countries & Platform Exclusivity
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), dpi=300, facecolor='#0B132B')

# Top 6 Countries
countries = df['Country'].dropna().str.split(',').explode().str.strip().value_counts().head(6)
ax1.set_facecolor('#141F38')
bars_c = ax1.barh(countries.index[::-1], countries.values[::-1], color='#38BDF8', edgecolor='#0B132B', height=0.6)
ax1.set_title('Top Movie Producing Countries', fontsize=10, fontweight='bold', color='#FFFFFF', pad=10)
ax1.set_xlabel('Movie Count', fontsize=9, color='#E2E8F0')
ax1.grid(axis='x', linestyle='--', alpha=0.3)
for b in bars_c:
    w = b.get_width()
    ax1.text(w + 100, b.get_y() + b.get_height()/2, f'{w:,}', ha='left', va='center', fontsize=8, color='#FFFFFF')

# Exclusivity Pie
df['platform_count'] = df['Netflix'] + df['Hulu'] + df['Prime Video'] + df['Disney+']
exclusive_counts = [df['platform_count'].eq(1).sum(), df['platform_count'].gt(1).sum()]
ex_labels = [f'Exclusive ({exclusive_counts[0]:,})', f'Shared ({exclusive_counts[1]:,})']
ex_colors = ['#F59E0B', '#3B82F6']
wedges, texts, autotexts = ax2.pie(
    exclusive_counts,
    labels=ex_labels,
    colors=ex_colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.7,
    textprops=dict(color='#FFFFFF', fontsize=8),
    wedgeprops=dict(width=0.45, edgecolor='#0B132B', linewidth=2)
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_weight('bold')
ax2.set_title('Catalog Licensing Exclusivity', fontsize=10, fontweight='bold', color='#FFFFFF', pad=10)

plt.suptitle('Figure 6: Geographic Origin & Platform Content Licensing Exclusivity', fontsize=11, fontweight='bold', color='#38BDF8', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "fig6_country_exclusivity.png"), dpi=300)
plt.close()
print("Saved fig6_country_exclusivity.png")

print("All 6 publication figures generated successfully!")
