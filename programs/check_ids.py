import fetch_id_rank
import fetch_num_id
import json

from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

dict_id_rank = fetch_id_rank.func_id_rank()
dict_num_id = fetch_num_id.func_num_id()

for k,v in dict_num_id.items():
    dict_id_rank[dict_num_id[k]] = dict_id_rank.pop(k)


listOfLists = [[]]
for k,v in dict_id_rank.items():
    listOfIds = []
    listOfIds.append(k)
    for itm in v:
        for key in itm.keys():
            listOfIds.append(key)
    listOfLists.append(listOfIds)
all_id_list = []
for x in range(len(listOfLists)):
    for y in range(len(listOfLists[x])):
        all_id_list.append(listOfLists[x][y])
listOfLists.pop(0)

outF1 = open("./data/found_ids.txt", "w")
outF2 = open("./data/not_found_ids.txt", "w")
for id in all_id_list:
    res = es.search(index="trec_news", body={"query": {"match": {'_id':id}}})
    if res['hits']['total'] == 0:
        outF2.write(str(id))
        outF2.write("\n")
    else:
        outF1.write(str(res['hits']['hits'][0]['_id']))
        outF1.write("\n")
outF1.close()
outF2.close()            