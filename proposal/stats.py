import pandas as pd

# Load the ATP data
atp_data = pd.read_csv('cleaned_ATP_Men.csv')

# Load the WTA data
wta_data = pd.read_csv('cleaned_ATP_Men.csv')

# Drop rows with missing values in age columns
atp_data_cleaned = atp_data.dropna(subset=['winner_age', 'loser_age'])
wta_data_cleaned = wta_data.dropna(subset=['winner_age', 'loser_age'])

# Convert age columns to numeric values
atp_data_cleaned['winner_age'] = pd.to_numeric(atp_data_cleaned['winner_age'], errors='coerce')
atp_data_cleaned['loser_age'] = pd.to_numeric(atp_data_cleaned['loser_age'], errors='coerce')
wta_data_cleaned['winner_age'] = pd.to_numeric(wta_data_cleaned['winner_age'], errors='coerce')
wta_data_cleaned['loser_age'] = pd.to_numeric(wta_data_cleaned['loser_age'], errors='coerce')

# Drop rows where age conversion resulted in NaN
atp_data_cleaned = atp_data_cleaned.dropna(subset=['winner_age', 'loser_age'])
wta_data_cleaned = wta_data_cleaned.dropna(subset=['winner_age', 'loser_age'])

# Calculate statistics for ATP data
atp_winner_above_30 = (atp_data_cleaned['winner_age'] > 30).mean() * 100
atp_loser_above_30 = (atp_data_cleaned['loser_age'] > 30).mean() * 100

atp_winner_avg_age = atp_data_cleaned['winner_age'].mean()
atp_loser_avg_age = atp_data_cleaned['loser_age'].mean()

atp_winner_median_age = atp_data_cleaned['winner_age'].median()
atp_loser_median_age = atp_data_cleaned['loser_age'].median()

atp_age_difference = (atp_data_cleaned['winner_age'] - atp_data_cleaned['loser_age']).mean()

# Calculate statistics for WTA data
wta_winner_above_30 = (wta_data_cleaned['winner_age'] < 21).mean() * 100
wta_loser_above_30 = (wta_data_cleaned['loser_age'] < 21).mean() * 100

wta_winner_avg_age = wta_data_cleaned['winner_age'].mean()
wta_loser_avg_age = wta_data_cleaned['loser_age'].mean()

wta_winner_median_age = wta_data_cleaned['winner_age'].median()
wta_loser_median_age = wta_data_cleaned['loser_age'].median()

wta_age_difference = (wta_data_cleaned['winner_age'] - wta_data_cleaned['loser_age']).mean()

# Print the results
print(f"Percentage of ATP winners above 30: {atp_winner_above_30:.2f}%")
print(f"Percentage of ATP losers above 30: {atp_loser_above_30:.2f}%")
print(f"Average age of ATP winners: {atp_winner_avg_age:.2f}")
print(f"Average age of ATP losers: {atp_loser_avg_age:.2f}")
print(f"Median age of ATP winners: {atp_winner_median_age:.2f}")
print(f"Median age of ATP losers: {atp_loser_median_age:.2f}")
print(f"Average age difference in ATP matches: {atp_age_difference:.2f}")

print(f"\nPercentage of WTA winners above 30: {wta_winner_above_30:.2f}%")
print(f"Percentage of WTA losers above 30: {wta_loser_above_30:.2f}%")
print(f"Average age of WTA winners: {wta_winner_avg_age:.2f}")
print(f"Average age of WTA losers: {wta_loser_avg_age:.2f}")
print(f"Median age of WTA winners: {wta_winner_median_age:.2f}")
print(f"Median age of WTA losers: {wta_loser_median_age:.2f}")
print(f"Average age difference in WTA matches: {wta_age_difference:.2f}")

wta_data_cleaned = wta_data[['winner_age', 'loser_age', 'surface']].dropna()

# Converteer leeftijdsgegevens naar numeriek
wta_data_cleaned['winner_age'] = pd.to_numeric(wta_data_cleaned['winner_age'], errors='coerce')
wta_data_cleaned['loser_age'] = pd.to_numeric(wta_data_cleaned['loser_age'], errors='coerce')

# Beschrijvende statistieken voor leeftijdsvariabelen
winner_age_stats = wta_data_cleaned['winner_age'].describe()
loser_age_stats = wta_data_cleaned['loser_age'].describe()

# Percentage speelsters ouder dan 30 jaar
percentage_winners_above_30 = (wta_data_cleaned['winner_age'] > 30).mean() * 100
percentage_losers_above_30 = (wta_data_cleaned['loser_age'] > 30).mean() * 100

# Verdeling van de ondergrond typen
surface_distribution = wta_data_cleaned['surface'].value_counts(normalize=True) * 100

# Resultaten weergeven
print(winner_age_stats, loser_age_stats, percentage_winners_above_30, percentage_losers_above_30, surface_distribution)