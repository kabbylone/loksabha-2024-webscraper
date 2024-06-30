import json
import csv

with open('kalvium/spiders/statewise_elections.json', 'r') as f:
    data = json.load(f)

csv_file = 'statewise-elections.csv'

headers = data[0].keys()

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print(f'CSV file "{csv_file}" has been created successfully.')
