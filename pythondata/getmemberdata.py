#Toby, Ruha, Carlos
#Read superheroes.json
import json

with open('superheroes.json', 'r') as f:
	squad = json.load(f)
	members = squad['members']	

#Write a header to CSV file
import csv


with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])

#Loop over members and write csv
	for squadmember in members:
		powers = squadmember['powers']
		for power in powers:
			print(power)
			writer = csv.writer(f)
			writer.writerow([squadmember['name'], squadmember['age'], squadmember['secretIdentity'], power, squad['squadName'], squad['homeTown'], squad['formed'], squad['secretBase'], squad['active']])
		