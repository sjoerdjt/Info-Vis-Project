import pandas as pd

# Laad de datasets
atp_data = pd.read_csv('original_datasets/ATP_Men - Sheet1.csv')
wta_data = pd.read_csv('original_datasets/wta_matches_2022.csv')

# Functie om de nodige bewerkingen op elke dataset uit te voeren
def preprocess_data(data, gender):
    # Verwijderen van kolommen die van belang zijn (alleen wanneer ze data missen)
    columns_to_drop = ['winner_entry', 'loser_entry', 'winner_seed', 'loser_seed']
    data = data.drop(columns=columns_to_drop, errors='ignore')
    
    # Omzetten van tourney_date naar datetime
    data['tourney_date'] = pd.to_datetime(data['tourney_date'], format='%Y%m%d')
    
    # Verwijderen van rijen met ontbrekende 'winner_age', 'loser_age', 'winner_ht' of 'loser_ht'
    data = data.dropna(subset=['winner_age', 'loser_age', 'winner_ht', 'loser_ht'])
    
    # Controleren of de leeftijdskolommen van het type object zijn en vervangen van komma's door punten
    if data['winner_age'].dtype == object:
        data['winner_age'] = pd.to_numeric(data['winner_age'].str.replace(',', '.'))
    if data['loser_age'].dtype == object:
        data['loser_age'] = pd.to_numeric(data['loser_age'].str.replace(',', '.'))
    
    # Als de kolommen al numeriek zijn
    if data['winner_age'].dtype != object:
        data['winner_age'] = pd.to_numeric(data['winner_age'])
    if data['loser_age'].dtype != object:
        data['loser_age'] = pd.to_numeric(data['loser_age'])
    
    # Toevoegen van de 'gender' kolom zodat datasets gecombineerd kunnen worden
    data['gender'] = gender
    
    return data

# Toepassen van de functie op beide datasets
atp_data_cleaned = preprocess_data(atp_data, 'Men')
wta_data_cleaned = preprocess_data(wta_data, 'Women')

# Combineren van de datasets
combined_data = pd.concat([atp_data_cleaned, wta_data_cleaned], ignore_index=True)

# Opslaan van de gecombineerde dataset
combined_data.to_csv('cleaned_datasets/combined_cleaned_tennis_data.csv', index=False)

