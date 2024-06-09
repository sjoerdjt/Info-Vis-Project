import pandas as pd

# Laad de ATP dataset
atp_data = pd.read_csv('datasets/ATP_Men - Sheet1.csv')

# Laad de WTA dataset
wta_data = pd.read_csv('datasets/wta_matches_2022.csv')

# Definieer een functie om de dataset op te schonen
def clean_dataset(df):
    # Verwijder rijen met ontbrekende waarden in essentiële kolommen
    essential_columns = ['winner_age', 'loser_age', 'winner_rank', 'loser_rank']
    df = df.dropna(subset=essential_columns)
    
    # Converteer kolommen naar het juiste datatype
    df.loc[:, 'winner_age'] = pd.to_numeric(df['winner_age'], errors='coerce')
    df.loc[:, 'loser_age'] = pd.to_numeric(df['loser_age'], errors='coerce')
    df.loc[:, 'winner_rank'] = pd.to_numeric(df['winner_rank'], errors='coerce')
    df.loc[:, 'loser_rank'] = pd.to_numeric(df['loser_rank'], errors='coerce')
    df.loc[:, 'tourney_date'] = pd.to_datetime(df['tourney_date'], errors='coerce', format='%Y%m%d')
    
    # Vul ontbrekende waarden in 'winner_hand' en 'loser_hand' met 'Unknown'
    df['winner_hand'].fillna('Unknown', inplace=True)
    df['loser_hand'].fillna('Unknown', inplace=True)
    
    # Vul ontbrekende waarden in 'winner_ht' en 'loser_ht' met de gemiddelde waarde van hun respectieve kolommen
    df['winner_ht'].fillna(df['winner_ht'].mean(), inplace=True)
    df['loser_ht'].fillna(df['loser_ht'].mean(), inplace=True)
    
    # Vul ontbrekende waarden in andere numerieke kolommen met 0
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    non_essential_numeric_columns = [col for col in numeric_columns if col not in essential_columns]
    df[non_essential_numeric_columns] = df[non_essential_numeric_columns].fillna(0)
    
    return df

# Maak de datasets schoon
atp_data_cleaned = clean_dataset(atp_data)
wta_data_cleaned = clean_dataset(wta_data)

# Sla de opgeschoonde datasets op
atp_data_cleaned.to_csv('cleaned_ATP_Men.csv', index=False)
wta_data_cleaned.to_csv('cleaned_WTA_Women.csv', index=False)

# Inspecteer de opgeschoonde datasets
print("ATP Data Summary (Cleaned):")
print(atp_data_cleaned.describe(include='all'))

print("WTA Data Summary (Cleaned):")
print(wta_data_cleaned.describe(include='all'))
