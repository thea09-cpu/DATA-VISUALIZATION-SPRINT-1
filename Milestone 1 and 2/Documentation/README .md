# Sports Performance Analytics Visualization System

A data analytics and visualization pipeline built on esports match data, developed as part of SDS 2206: Data Visualization Analytics and Reporting.

## Description

This project implements an end-to-end sports performance analytics system using a structured esports dataset containing player and match statistics. The system ingests raw CSV data, cleans and validates it through a reproducible pipeline, engineers meaningful performance features, and produces a suite of visualizations covering player roles, team combat stats, fatigue, reaction time, and win probability. It is designed to evolve across six milestones — from raw data representation through to interactive dashboards and advanced analytics — making it suitable for both academic reporting and practical performance analysis in competitive esports contexts.

## Getting Started

### Dependencies

* Python 3.8 or higher
* Windows 10 / macOS 12+ / Ubuntu 20.04+
* Required Python libraries:
  * `pandas` — data loading, cleaning, and aggregation
  * `numpy` — numerical operations and range validation
  * `matplotlib` — chart generation and visualization output

Install all dependencies with:

```
pip install pandas numpy matplotlib
```

### Installing

1. Clone or download this repository to your local machine
2. Place your raw dataset file inside the following folder (create it if it does not exist):

```
Data/Raw/esports dataset.csv
```

3. Ensure the output directories exist or let the scripts create them automatically:

```
data/processed/
visuals/
```

### Executing the Program

**Step 1 — Run the data pipeline (cleaning, validation, feature engineering):**

```
python main.py
```

This will:
* Load the raw dataset from `Data/Raw/`
* Remove duplicates and standardize categorical labels
* Validate numerical columns against defined range rules
* Impute missing values and engineer KDA, kill-death difference, and MVP features
* Save the cleaned dataset to `data/processed/cleaned_esports_data.csv`
* Generate and save initial visualizations to `visuals/`

**Step 2 — Run the analysis and extended visualization script:**

```
python data_analysis.py
```

This will:
* Load the cleaned dataset
* Compute descriptive statistics (mean, variance, distributions)
* Generate team-level aggregations and role/map breakdowns
* Output charts including scatter plots, histograms, and grouped bar charts to `visuals/`

## Help

**Issue: FileNotFoundError when loading the dataset**
Ensure the raw CSV file is named exactly `esports dataset.csv` (with a space) and is placed inside `Data/Raw/`. The folder names are case-sensitive on Linux/macOS.

**Issue: Charts display but do not save**
Confirm that the `visuals/` directory exists or has write permissions. The scripts call `os.makedirs("visuals", exist_ok=True)` automatically, but permission errors on restricted systems may prevent folder creation.

**Issue: MVP binary column is_mvp contains NaN**
Rows where `mvp_award` could not be mapped to 'yes' or 'no' after standardization are set to NaN. Review the raw data for unusual label variants not covered by the current mapping.

```
python main.py --help
```

## Authors

*  Stephen Mwangi - SCT213-C002-0089/2024
*  Cynthia Mueni - SCT213-C002-0043/2024
*  Eric Ndiritu - SCT213-C002-0003/2024
*  Sharif Aziz - SCT213-C002-0084/2024
*  Fatma Habona - SCT213-C002-0001/2024
*  Victor Karanja- SCT213-C002-0042/2024
*  Mercy Jeptoo - SCT213-C002-0103/2024
*  Sharon Bundi - SCT213-C002-0042/2024
*  Norah Kigen - SCT213-C002-0085/2024

## Version History

* **0.2**
  * Added extended visualization script (`data_analysis.py`)
  * Added team-level aggregation, fatigue analysis, and reaction time boxplot
  * Range validation and anomaly handling added to pipeline
  * See [release history](#)

* **0.1**
  * Initial release
  * Raw data loading, basic cleaning, kills histogram, and MVP bar chart (`main.py`)

## License

This project is licensed under the MIT License — see the `LICENSE.md` file for details.

## Acknowledgments

* [Pandas Documentation](https://pandas.pydata.org/docs/) — data manipulation and cleaning reference
* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — visualization implementation
* [Awesome README](https://github.com/matiassingers/awesome-readme) — README structure inspiration
* [PurpleBooth README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) — template reference
* SDS 2206 course material — Seth Kipsang, program structure and milestone framework
