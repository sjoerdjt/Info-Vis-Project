import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Laad de dataset
df = pd.read_csv('/atp_data.csv')

# Voeg een kolom toe om te markeren of de speler de wedstrijd heeft gewonnen
df['win'] = 1  # Aangezien de gegevens per wedstrijd zijn en de winnaar is al bekend, markeren we alle rijen als gewonnen voor de winnaar

# Scatter plot van elo_winner versus wedstrijdresultaat
plt.figure(figsize=(10, 6))
sns.scatterplot(x='elo_winner', y='win', data=df)
plt.title('Impact van Elo-score op het Winnen van Wedstrijden')
plt.xlabel('Elo-score van de Winnaar')
plt.ylabel('Wedstrijd Gewonnen (1=Ja)')
plt.show()


