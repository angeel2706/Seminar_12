import json
import matplotlib.pyplot as plt 


with open('data.json') as json_file:
    data = json.load(json_file)
   
print(len(data))

plt.hist(data, bins = 10)

plt.show()