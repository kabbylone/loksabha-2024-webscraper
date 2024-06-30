import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

df = pd.read_csv('statewise-elections.csv')

report = df.groupby(['State', 'Party'])['Won'].sum().reset_index()

pivot_table = report.pivot(index='State', columns='Party', values='Won').fillna(0)

parties = pivot_table.columns

party_colors = {}
for party in parties:
    party_colors[party] = mcolors.to_hex(tuple(random.uniform(0, 1) for _ in range(3)))

pivot_table.plot(kind='bar', stacked=True, figsize=(14, 8), color=[party_colors[party] for party in parties])
plt.title('Seats Won by Each Party in Each State')
plt.xlabel('State')
plt.ylabel('Seats Won')
plt.legend(title='Party', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
