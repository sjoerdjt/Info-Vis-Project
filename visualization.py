import pandas as pd
data = pd.read_csv('cleaned_datasets/combined_cleaned_tennis_data.csv')


from matplotlib import pyplot as plt
data['winner_ht'].plot(kind='hist', bins=20, title='winner_ht')
plt.gca().spines[['top', 'right',]].set_visible(False)


from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('surface').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

plt.show()

