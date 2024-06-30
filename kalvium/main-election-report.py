import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open('spiders\main-election.json', 'r') as file:
    json_data = json.load(file)

df = pd.DataFrame(json_data)

df['Won'] = pd.to_numeric(df['Won'])
df['Leading'] = pd.to_numeric(df['Leading'])
df['Total'] = pd.to_numeric(df['Total'])

df_sorted = df.sort_values(by='Won', ascending=False)

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
sns.barplot(y='Party', x='Won', data=df_sorted, palette='viridis')
plt.xlabel('Number of Seats Won')
plt.ylabel('Political Party')
plt.title('Number of Seats Won by Each Political Party')
plt.show()

top_10_df = df_sorted.head(10)
plt.figure(figsize=(10, 10))
plt.pie(top_10_df['Won'], labels=top_10_df['Party'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(top_10_df)))
plt.title('Proportion of Seats Won by Top 10 Political Parties')
plt.axis('equal')  
plt.show()
