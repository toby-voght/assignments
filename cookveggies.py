#Read vegetables.csv
import csv
import json

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader]

with open('vegetables.json', 'w') as f:
	json.dump(vegetables, f, indent=2)