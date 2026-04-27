import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output directories if they don't exist
os.makedirs("visuals", exist_ok=True)
os.makedirs(os.path.join("data", "processed"), exist_ok=True)

# --- 1) Load cleaned dataset ---
df = pd.read_csv("data/processed/cleaned_esports_data.csv")

# --- 2) Basic descriptive statistics ---
print("\n--- Basic Statistics ---")
print(df.describe(include='all'))   # summary for numeric + categorical
print("\nVariance of numeric columns:\n", df.var(numeric_only=True))

# --- 3) Team-level statistics ---
if 'team_name' in df.columns:
    team_stats = df.groupby('team_name')[['kills','assists','deaths']].sum()
    print("\nKills, Assists, Deaths per Team:\n", team_stats)

    team_stats.plot(kind='bar', figsize=(10,6))
    plt.title("Kills, Assists, Deaths per Team")
    plt.xlabel("Team")
    plt.ylabel("Total Count")
    plt.tight_layout()
    plt.savefig("visuals/team_kills_assists_deaths.png")
    plt.show()

# --- 4) Accuracy vs Win Probability ---
if 'accuracy_percent' in df.columns and 'win_probability' in df.columns:
    plt.figure(figsize=(8,6))
    plt.scatter(df['accuracy_percent'], df['win_probability'], alpha=0.5, color='purple')
    plt.title("Accuracy vs Win Probability")
    plt.xlabel("Accuracy (%)")
    plt.ylabel("Win Probability")
    plt.tight_layout()
    plt.savefig("visuals/accuracy_vs_winprob.png")
    plt.show()

# --- 5) Player Role Analysis ---
if 'player_role' in df.columns:
    role_stats = df['player_role'].value_counts()
    print("\nPlayer Role Counts:\n", role_stats)

    role_stats.plot(kind='bar', color='skyblue')
    plt.title("Distribution of Player Roles")
    plt.xlabel("Role")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("visuals/player_roles.png")
    plt.show()

# --- 6) Map Played Analysis ---
if 'map_played' in df.columns:
    map_stats = df['map_played'].value_counts()
    print("\nMap Played Counts:\n", map_stats)

    map_stats.plot(kind='bar', color='orange')
    plt.title("Distribution of Maps Played")
    plt.xlabel("Map")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("visuals/maps_played.png")
    plt.show()

# --- 7) Fatigue Index Analysis ---
if 'fatigue_index' in df.columns:
    plt.figure(figsize=(8,6))
    plt.hist(df['fatigue_index'], bins=20, color='red', edgecolor='white')
    plt.title("Fatigue Index Distribution")
    plt.xlabel("Fatigue Index")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("visuals/fatigue_index_distribution.png")
    plt.show()

    # Compare fatigue index vs performance score
    if 'performance_score' in df.columns:
        plt.figure(figsize=(8,6))
        plt.scatter(df['fatigue_index'], df['performance_score'], alpha=0.5, color='green')
        plt.title("Fatigue Index vs Performance Score")
        plt.xlabel("Fatigue Index")
        plt.ylabel("Performance Score")
        plt.tight_layout()
        plt.savefig("visuals/fatigue_vs_performance.png")
        plt.show()
