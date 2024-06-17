import pandas as pd
import plotly.express as px

# Het aantal procent van de wedstrijden dat gewonnen is van een rechtshandige man/vrouw vs. linkshandige man/vrouw in een boxplot.
# Creëer dummydata
data = {
    'Player': ['Player1', 'Player2', 'Player3', 'Player4', 'Player5', 'Player6', 'Player7', 'Player8'],
    'Gender': ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
    'Handedness': ['Right', 'Left', 'Right', 'Left', 'Right', 'Left', 'Right', 'Left'],
    'Wins': [23, 15, 18, 20, 25, 12, 30, 14]
}

# Zet de data om in een DataFrame
df = pd.DataFrame(data)

# Maak een boxplot met plotly
fig = px.box(df, x='Handedness', y='Wins', color='Gender', title='Wins by Handedness and Gender in Tennis',
             labels={'Handedness': 'Handedness', 'Wins': 'Number of Wins'})

# Toon de plot
fig.show()

















# Dummydata creëren
np.random.seed(42)
ages = np.arange(18, 36)

# Aantal gewonnen wedstrijden met een piek rond een optimale leeftijd (bijvoorbeeld 25 jaar)
wins_men = -0.5 * (ages - 25)**2 + np.random.normal(scale=5, size=len(ages)) + 50
wins_women = -0.5 * (ages - 23)**2 + np.random.normal(scale=5, size=len(ages)) + 50

# Data omzetten in een DataFrame
df = pd.DataFrame({
    'Age': np.concatenate([ages, ages]),
    'Wins': np.concatenate([wins_men, wins_women]),
    'Gender': ['M'] * len(ages) + ['F'] * len(ages)
})

# Plotly figuur maken
fig = go.Figure()

# Curve voor mannen
fig.add_trace(go.Scatter(x=ages, y=wins_men, mode='lines+markers', name='Men', line=dict(color='blue')))

# Curve voor vrouwen
fig.add_trace(go.Scatter(x=ages, y=wins_women, mode='lines+markers', name='Women', line=dict(color='red')))

# Layout aanpassen
fig.update_layout(
    title='Wins by Age and Gender in Tennis',
    xaxis_title='Age',
    yaxis_title='Number of Wins',
    legend_title='Gender'
)

# Toon de plot
fig.show()





















# Dummydata creëren
np.random.seed(42)
n_matches = 100

# Ranglijsten van de spelers (bijvoorbeeld 1 tot 100)
rankings = np.random.randint(1, 101, size=n_matches)

# Winnen of verliezen (0 = verliezen, 1 = winnen)
# Simuleren dat hogere rang (kleinere ranking) meer kans heeft om te winnen
wins = np.random.binomial(1, p=(101 - rankings) / 101)

# Data omzetten in een DataFrame
df = pd.DataFrame({
    'Ranking': rankings,
    'Wins': wins
})

# Plotly scatter plot maken
fig = px.scatter(df, x='Ranking', y='Wins', title='Match Outcomes Based on Player Ranking',
                 labels={'Ranking': 'Player Ranking', 'Wins': 'Match Outcome'},
                 color='Wins', color_continuous_scale=['red', 'green'], 
                 category_orders={"Wins": [0, 1]})

# Layout aanpassen
fig.update_layout(
    xaxis=dict(title='Player Ranking (1 = best)'),
    yaxis=dict(title='Match Outcome (0 = Loss, 1 = Win)'),
    coloraxis_showscale=False
)

# Toon de plot
fig.show()



