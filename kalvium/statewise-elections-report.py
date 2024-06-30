import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

# Load CSV file into a DataFrame
df = pd.read_csv('statewise-elections.csv')

# Group by 'State' and 'Party' columns and sum the 'Won' seats
report = df.groupby(['State', 'Party'])['Won'].sum().reset_index()

# Pivot the DataFrame to prepare for plotting
pivot_table = report.pivot(index='State', columns='Party', values='Won').fillna(0)

# Get list of parties
parties = pivot_table.columns

# Generate random unique colors for each party
party_colors = {}
for party in parties:
    party_colors[party] = mcolors.to_hex(tuple(random.uniform(0, 1) for _ in range(3)))

# Plotting
pivot_table.plot(kind='bar', stacked=True, figsize=(14, 8), color=[party_colors[party] for party in parties])
plt.title('Seats Won by Each Party in Each State')
plt.xlabel('State')
plt.ylabel('Seats Won')
plt.legend(title='Party', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
