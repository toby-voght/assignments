#Toby and Simon

#Read vegtables.csv into a variable called vegtables.
import csv
import json

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader]

#Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for vegetable in vegetables:
    color = vegetable['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(vegetable)
    else:
        vegetables_by_color[color] = [vegetable]

print(vegetables_by_color)
#Output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegetables_by_color.json', 'w') as g:
	json.dump(vegetables_by_color, g, indent = 2)