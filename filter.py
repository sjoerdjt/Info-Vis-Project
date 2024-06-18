import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv('combined_cleaned_tennis_data - combined_cleaned_tennis_data.csv.csv')

grouped_winnaars = data.groupby(['w_ace', 'w_df']).size().reset_index(name='frequency')
grouped_verliezers = data.groupby(['l_ace', 'l_df']).size().reset_index(name='frequency')

grouped_winnaars['adjusted_size'] = np.sqrt(grouped_winnaars['frequency']) * 10 / (1 + 0.1 * grouped_winnaars['w_ace'] + 0.1 * grouped_winnaars['w_df'])
grouped_verliezers['adjusted_size'] = np.sqrt(grouped_verliezers['frequency']) * 10 / (1 + 0.1 * grouped_verliezers['l_ace'] + 0.1 * grouped_verliezers['l_df'])

fig_winnaars = px.scatter(grouped_winnaars,
                          x='w_ace',
                          y='w_df',
                          size='adjusted_size',
                          color='frequency',
                          hover_data={'frequency': True, 'w_ace': True, 'w_df': True, 'adjusted_size': False},
                          title='Bubble Plot Aces vs. Dubbele Fouten (Winnaars)',
                          labels={'w_ace': 'Aantal Aces', 'w_df': 'Aantal Dubbele Fouten', 'frequency': 'Frequentie'},
                          size_max=22,
                          opacity=0.8,
                          color_continuous_scale=px.colors.sequential.Viridis)

fig_winnaars.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
fig_winnaars.update_layout(plot_bgcolor='white', 
                           xaxis=dict(title='Aantal Aces', range=[-1, 41]),
                           yaxis=dict(title='Aantal Dubbele Fouten', range=[-1, 21]),
                           margin=dict(l=20, r=20, t=60, b=20))

fig_verliezers = px.scatter(grouped_verliezers,
                            x='l_ace',
                            y='l_df',
                            size='adjusted_size',
                            color='frequency',
                            hover_data={'frequency': True, 'l_ace': True, 'l_df': True, 'adjusted_size': False},
                            title='Bubble Plot Aces vs. Dubbele Fouten (Verliezers)',
                            labels={'l_ace': 'Aantal Aces', 'l_df': 'Aantal Dubbele Fouten', 'frequency': 'Frequentie'},
                            size_max=22,
                            opacity=0.8,
                            color_continuous_scale=px.colors.sequential.Viridis)

fig_verliezers.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
fig_verliezers.update_layout(plot_bgcolor='white', 
                             xaxis=dict(title='Aantal Aces', range=[-1, 41]),
                             yaxis=dict(title='Aantal Dubbele Fouten', range=[-1, 21]),
                             margin=dict(l=20, r=20, t=60, b=20))

fig_winnaars.show()
fig_verliezers.show()


import pandas as pd
import plotly.express as px

file_path = 'filtered_tennis_data.csv'
tennis_data = pd.read_csv(file_path)

rank_sum_per_country = tennis_data.groupby('winner_ioc')['winner_rank'].sum().reset_index()
rank_count_per_country = tennis_data.groupby('winner_ioc')['winner_rank'].count().reset_index()

rank_data = pd.merge(rank_sum_per_country, rank_count_per_country, on='winner_ioc')
rank_data.columns = ['Land', 'Total_Rank', 'Player_Count']

rank_data['Gemiddelde Rank'] = rank_data['Total_Rank'] / rank_data['Player_Count']

average_rank_per_country = rank_data[['Land', 'Gemiddelde Rank']]

fig = px.choropleth(
    average_rank_per_country,
    locations="Land",
    locationmode="ISO-3",
    color="Gemiddelde Rank",
    hover_name="Land",
    hover_data=["Gemiddelde Rank"],
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Gemiddelde Rank Per Land"
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="Gemiddelde Rank"
    )
)

fig.show()

# Create a set to keep track of seen players
seen_players = set()

# Define a function to check if a player has been seen before
def has_been_seen(row):
    if row['winner_name'] in seen_players or row['loser_name'] in seen_players:
        return True
    seen_players.add(row['winner_name'])
    seen_players.add(row['loser_name'])
    return False

# Apply the function to filter the DataFrame
filtered_data = tennis_data[~tennis_data.apply(has_been_seen, axis=1)]

# Define the output file path
filtered_file_path = '/mnt/data/filtered_tennis_data.csv'

# Save the filtered DataFrame to a CSV file
filtered_data.to_csv(filtered_file_path, index=False)

filtered_file_path