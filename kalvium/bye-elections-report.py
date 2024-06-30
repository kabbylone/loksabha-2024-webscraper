import json

# Load data from JSON file
with open('spiders/bye-elections.json', 'r') as f:
    data = json.load(f)

from collections import defaultdict

# Initialize a dictionary to count bye-election wins by party initials
party_wins = defaultdict(int)

# Count bye-elections won by each party
for entry in data:
    party = entry['Party']
    # Get initials of the party
    initials = ''.join(word[0].upper() for word in party.split())
    party_wins[initials] += 1

import matplotlib.pyplot as plt
import numpy as np

# Extract parties and their respective counts
parties = list(party_wins.keys())
counts = list(party_wins.values())

# Generate random colors for each party
colors = np.random.rand(len(parties), 3)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(parties, counts, color=colors)

# Adding labels and title
plt.xlabel('Parties')
plt.ylabel('Number of Bye-Elections Won')
plt.title('Bye-Elections Won by Each Party')

# Adding counts on top of each bar
for bar, count in zip(bars, counts):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, count, ha='center', va='bottom')

# Show plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
