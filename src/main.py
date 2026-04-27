import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1) Load dataset ---
df = pd.read_csv(os.path.join("Data", "Raw", "esports dataset.csv"))

# --- 2) Basic info ---
print("Shape (rows, columns):", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nMissing values per column:\n", df.isna().sum())
print("\nFirst 5 rows:\n", df.head())

# --- 3) Cleaning ---
df_clean = df.copy()

# Remove duplicates
df_clean = df_clean.drop_duplicates()

# Standardize string columns
str_cols = ['team_name','player_role','map_played','match_type','match_outcome','mvp_award']
for col in str_cols:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].astype(str).str.strip().str.lower()
        df_clean[col] = df_clean[col].replace(['', 'none', 'null', 'nan'], np.nan)

# Convert numeric columns safely
num_cols = ['kills','assists','deaths','accuracy_percent','reaction_time_ms',
            'fatigue_index','performance_score','win_probability']
for col in num_cols:
    if col in df_clean.columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

# Flag impossible ranges (set to NaN)
range_rules = {
    'accuracy_percent': (0, 100),
    'win_probability': (0, 1),
    'fatigue_index': (0, 1),
    'reaction_time_ms': (80, 600),
    'kills': (0, 80),
    'assists': (0, 80),
    'deaths': (0, 80)
}
for col, (lo, hi) in range_rules.items():
    if col in df_clean.columns:
        bad_mask = df_clean[col].notna() & ((df_clean[col] < lo) | (df_clean[col] > hi))
        df_clean.loc[bad_mask, col] = np.nan

# Replace numeric missing values with 1 (keep object/string missing values as NaN)
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
if len(numeric_cols) > 0:
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(1)

# --- 4) Feature engineering ---
if all(c in df_clean.columns for c in ['kills','assists','deaths']):
    df_clean['kda_ratio'] = (df_clean['kills'] + df_clean['assists']) / df_clean['deaths'].replace(0, np.nan)
    df_clean['kill_death_diff'] = df_clean['kills'] - df_clean['deaths']

# Standardize MVP award values to yes/no and create a binary flag
if 'mvp_award' in df_clean.columns:
    df_clean['mvp_award'] = df_clean['mvp_award'].replace({
        'y': 'yes', 'true': 'yes', '1': 'yes',
        'n': 'no', 'false': 'no', '0': 'no',
        'award': 'yes', 'no award': 'no'
    })
    df_clean.loc[~df_clean['mvp_award'].isin(['yes', 'no']), 'mvp_award'] = np.nan
    df_clean['is_mvp'] = (df_clean['mvp_award'] == 'yes').astype('Int64')

# --- 5) Save cleaned dataset ---
os.makedirs(os.path.join("data", "processed"), exist_ok=True)
os.makedirs(os.path.join("visuals"), exist_ok=True)
df_clean.to_csv(os.path.join("data", "processed", "cleaned_esports_data.csv"), index=False)
print("\nCleaned dataset saved to data/processed/cleaned_esports_data.csv")

# --- 6) Visualization ---
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histogram of kills
axes[0].hist(df_clean['kills'].dropna(), bins=25, color="#3DAB2E", edgecolor='black')
axes[0].set_title('Kills Distribution (Cleaned)')
axes[0].set_xlabel('Kills')
axes[0].set_ylabel('Count')

# --- Bar chart of MVP awards (yes vs no) ---
award_counts = df_clean['mvp_award'].value_counts(dropna=False)

axes[1].bar(award_counts.index.astype(str), award_counts.values,
            color=["#491fb4", "#0eff0e"][:len(award_counts)])
axes[1].set_title('MVP Award Counts (yes/no)')
axes[1].set_xlabel('mvp_award')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.savefig("visuals/Kills and MVP Awards.png")
plt.show()

print("\nVisualization saved to visuals/Kills and MVP Awards.png")
