import numpy as np
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


list_of_scores = []
list_of_similarities = []
list_of_dict = []
with open('./data/GraphData.txt') as f:
    for line in f:
        str1 = str(line).replace("\n",'')
        str1 = str1.replace("\\n",'')
        dic1 = json.loads(str1)
        sim = float(dic1['similarity'])*100
        dic1['similarity'] = int(sim)
        list_of_dict.append(dic1)

sorted_list = sorted(list_of_dict, key = lambda i:i['similarity'], reverse = False)

for dic in sorted_list:
    list_of_scores.append(dic['score'])
    list_of_similarities.append(dic['similarity'])

plt.plot(list_of_similarities, list_of_scores)
plt.show()