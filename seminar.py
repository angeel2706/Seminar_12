import random
import json

data = list()
for i in range(1000):
	data.append(random.randint(0,101))

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)



