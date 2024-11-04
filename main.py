import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('dataset.csv')
platforms = ['PS4', 'XOne', 'PC', 'WiiU']
df_filtered = df[df['platform'].isin(platforms)]
df_platform_genre = df_filtered.groupby(['platform', 'genre']).size().reset_index(name='GameCount')

plt.figure(figsize=(12, 6))
sns.barplot(data=df_platform_genre, x='genre', y='GameCount', hue='platform')
plt.title('Number of Games by Genre per Platform')
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(
    data=df_platform_genre,
    x='genre',
    y='GameCount',
    hue='platform',
    palette='Set2',
    order=['Action', 'Adventure', 'Shooter', 'Sports']
)
plt.xlabel('Game Genre')
plt.ylabel('Number of Games')
plt.title('Number of Games by Genre per Platform')
plt.legend(title='platform', loc='upper right')
plt.show()
