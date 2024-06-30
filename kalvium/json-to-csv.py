import json
import csv

# Load data from JSON file
with open('kalvium\spiders\statewise_elections.json', 'r') as f:
    data = json.load(f)

# Specify the CSV file path
csv_file = 'statewise-elections.csv'

# Extract headers from the data (assuming all entries have the same keys)
headers = data[0].keys()

# Writing data to CSV
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print(f'CSV file "{csv_file}" has been created successfully.')
