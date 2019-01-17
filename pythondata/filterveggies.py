#Toby and Simon
#Read vegetables.csv into a variable called vegetables.
import csv
import json

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader]

print(vegetables)
#Loop through vegetables and filter down to only green vegtables using a whitelist.
veggies = []
greenveggies = ['green']
for vegetable in vegetables:
    if vegetable['color'] in greenveggies:
        veggies.append(vegetable)

#Print veggies to the terminal
print(veggies)

#Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as g:
	json.dump(veggies, g)