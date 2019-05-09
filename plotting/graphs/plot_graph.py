import numpy as np
import json
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


list_of_scores = []
list_of_similarities = []
list_of_dict = []
with open('GraphData.txt') as f:
    for line in f:
        str1 = str(line).replace("\n",'')
        str1 = str1.replace("\\n",'')
        dic1 = json.loads(str1)
        sim = float(dic1['similarity'])*100
        dic1['similarity'] = int(sim)
        dic1['score'] = int(dic1['score'])
        list_of_dict.append(dic1)

sorted_list = sorted(list_of_dict, key = lambda i:i['similarity'], reverse = False)

for dic in sorted_list:
    list_of_scores.append(dic['score'])
    list_of_similarities.append(dic['similarity'])

# plt.plot(list_of_similarities, list_of_scores)
# plt.show()


list_scores1 = []
list_sim1 = []
for x in range(len(list_of_scores)):
    if list_of_scores[x]  == 0:
        list_sim1.append(list_of_similarities[x])

list_index = []
for ind in range(len(list_sim1)):
    list_index.append(ind+1)
    ind+=1
#print(list_index)
plt.plot(list_sim1, list_index)
plt.title('Similarity plot for articles with score 0')
plt.xlabel('Percentage')
plt.ylabel('Index')

plt.show()        