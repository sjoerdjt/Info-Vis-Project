import pandas as pd

# Load the ATP data
atp_data = pd.read_csv('cleaned_ATP_Men.csv')

# Load the WTA data
wta_data = pd.read_csv('cleaned_WTA_Women.csv')

# Inspect the first few rows of both datasets
print("ATP Data:")
print(atp_data.head())

print("\nWTA Data:")
print(wta_data.head())

# Check for missing values in the ATP data
print("Missing values in ATP Data:")
print(atp_data[['winner_age', 'loser_age']].isnull().sum())

# Drop rows with missing values in age columns
atp_data_cleaned = atp_data.dropna(subset=['winner_age', 'loser_age'])

# Check for missing values in the WTA data
print("Missing values in WTA Data:")
print(wta_data[['winner_age', 'loser_age']].isnull().sum())

# Drop rows with missing values in age columns
wta_data_cleaned = wta_data.dropna(subset=['winner_age', 'loser_age'])

# Convert age columns to numeric values for ATP data
atp_data_cleaned['winner_age'] = pd.to_numeric(atp_data_cleaned['winner_age'], errors='coerce')
atp_data_cleaned['loser_age'] = pd.to_numeric(atp_data_cleaned['loser_age'], errors='coerce')

# Convert age columns to numeric values for WTA data
wta_data_cleaned['winner_age'] = pd.to_numeric(wta_data_cleaned['winner_age'], errors='coerce')
wta_data_cleaned['loser_age'] = pd.to_numeric(wta_data_cleaned['loser_age'], errors='coerce')

# Select relevant columns
variables = ['winner_rank', 'winner_age', 'loser_rank', 'loser_age']

# Calculate descriptive statistics for ATP data
atp_descriptive_stats = atp_data_cleaned[variables].describe()

# Calculate descriptive statistics for WTA data
wta_descriptive_stats = wta_data_cleaned[variables].describe()

# Display the results
print("\nATP Data Summary (Cleaned):")
print(atp_descriptive_stats)

print("\nWTA Data Summary:")
print(wta_descriptive_stats)
