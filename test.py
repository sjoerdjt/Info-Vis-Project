import pandas as pd

# Laad de opgeschoonde datasets
atp_data_cleaned = pd.read_csv('cleaned_ATP_Men.csv')
wta_data_cleaned = pd.read_csv('cleaned_WTA_Women.csv')

# Functie om basisinspecties uit te voeren
def inspect_dataset(df, dataset_name):
    print(f"Inspectie van {dataset_name} dataset:")
    
    # Basisstatistieken
    print("\nBasisstatistieken:")
    print(df.describe(include='all'))
    
    # Datatypes
    print("\nKolommen en datatypes:")
    print(df.dtypes)
    
    # Missende waarden
    print("\nAantal ontbrekende waarden per kolom:")
    print(df.isnull().sum())
    
    # Unieke waarden
    print("\nAantal unieke waarden per kolom:")
    print(df.nunique())
    
    # Range en distributie
    print("\nRange en distributie van numerieke kolommen:")
    print(df.describe())
    
    # Logische consistentie checken (bijv. winnaar rank <= verliezer rank)
    if 'winner_rank' in df.columns and 'loser_rank' in df.columns:
        inconsistent_ranks = df[df['winner_rank'] > df['loser_rank']]
        print(f"\nAantal inconsistenties in rang (winnaar rank > verliezer rank): {len(inconsistent_ranks)}")
    
    # Correlatieanalyse
    print("\nCorrelatiematrix:")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()
    print(correlation_matrix)

# Voer inspecties uit voor beide datasets
inspect_dataset(atp_data_cleaned, "ATP")
inspect_dataset(wta_data_cleaned, "WTA")

# Optioneel: Visualiseer de correlatiematrix
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df, dataset_name):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title(f'Correlatiematrix van {dataset_name} dataset')
    plt.show()

plot_correlation_matrix(atp_data_cleaned, "ATP")
plot_correlation_matrix(wta_data_cleaned, "WTA")
