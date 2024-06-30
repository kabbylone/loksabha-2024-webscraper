import json
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

with open('kalvium/spiders/bye-elections.json', 'r') as f:
    data = json.load(f)

party_wins = defaultdict(int)

for entry in data:
    party = entry['Party']
    initials = ''.join(word[0].upper() for word in party.split())
    party_wins[initials] += 1

parties = list(party_wins.keys())
counts = list(party_wins.values())

colors = np.random.rand(len(parties), 3)

plt.figure(figsize=(10, 6))
bars = plt.bar(parties, counts, color=colors)

plt.xlabel('Parties')
plt.ylabel('Number of Bye-Elections Won')
plt.title('Bye-Elections Won by Each Party')

for bar, count in zip(bars, counts):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, count, ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
