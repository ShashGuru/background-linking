import fetch_id_rank
import fetch_num_id
import json
from gensim.models.keyedvectors import KeyedVectors
from DocSim import DocSim
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

googlenews_model_path = './data/GoogleNews-vectors-negative300.bin'
stopwords_path = "./data/stopwords_en.txt"

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
#print(all_id_list)        
#print(dict_id_rank)
count_of_ids = 0
for e in range(len(listOfLists)):
    for f in range(len(listOfLists[e])):
        count_of_ids+=1
print(count_of_ids)        

all_id_list = list( dict.fromkeys(all_id_list) )



query = {
    "size" : 10000,
    "query": {
        "ids" : {
            "type" : "news_articles",
            "values" : all_id_list
        }
    }
}

res = es.search(index="trec_news", body=query, scroll='10m')
dict_of_docs = res['hits']['hits']

# with open("./data/output.json", 'r') as f:
#     dict_of_docs = json.load(f)

list_of_para = [[]]
for x in range(len(listOfLists)):
    list_of_id_docs = []
    for y in range(len(listOfLists[x])):
        for doc in dict_of_docs:
            if doc['_id'] == listOfLists[x][y]:
                list_of_id_docs.append(doc['_source']['paragraph'])
    list_of_para.append(list_of_id_docs)            
list_of_para.pop(0)

count_of_paras = 0
for g in range(len(list_of_para)):
    for h in range(len(list_of_para[g])):
        count_of_paras+=1
print(count_of_paras) 

#print(list_of_para)

model = KeyedVectors.load_word2vec_format(googlenews_model_path, binary=True)
with open(stopwords_path, 'r') as fh:
    stopwords = fh.read().split(",")
ds = DocSim(model,stopwords=stopwords)

count_comp_ids = 0
score_listOfLists= [[]]
for a in range(len(list_of_para)):
    list_id_score = []
    first_para = list_of_para[a][0]
    compare_list = []
    for b in range(len(list_of_para[a])):
        if b != 0:
            count_comp_ids+=1
            if(len(list_of_para[a][b]) == 0):
                list_of_para[a][b] = 'emptystring'
            list_of_para[a][b] = list_of_para[a][b].replace("\xad","-")
            list_of_para[a][b] = list_of_para[a][b].replace("\xa0"," ")
            list_of_para[a][b] = list_of_para[a][b].replace("\u2009"," ")     
            compare_list.append(list_of_para[a][b])
    sim_scores = ds.calculate_similarity(first_para, compare_list)
    for b in range(len(list_of_para[a])):  
        found_score = 0
        if b != 0:
            for score in sim_scores:
                if list_of_para[a][b] == score['doc']:
                    list_id_score.append(score['score'])
                    found_score = 1
                    break
            if found_score == 0:
                # print(listOfLists[a][0])
                # print(listOfLists[a][b])
                # print("\n")
                list_id_score.append(0)
    score_listOfLists.append(list_id_score) 
score_listOfLists.pop(0)
print(count_comp_ids)


count_of_scores = 0
for g in range(len(score_listOfLists)):
    for h in range(len(score_listOfLists[g])):
        count_of_scores+=1
print(count_of_scores)


list_of_all_scores = []
list_of_all_similarities = []
for c in range(len(listOfLists)):
    list_of_id_scores = []
    first_id = listOfLists[c][0]
    listOfCompIds = dict_id_rank[first_id]
    for d in range(len(listOfLists[c])): 
        if d != 0:
            list_of_all_similarities.append(score_listOfLists[c][d-1])
            cur_id = listOfLists[c][d]
            for it in listOfCompIds:
                for k,v in it.items():
                    if k == cur_id:
                        list_of_id_scores.append(v)
            #list_of_all_scores.append(listOfCompIds[)
    list_of_all_scores.append(list_of_id_scores)        

#outF = open("./data/GraphData.txt", "w")
# for i in range(len(list_of_all_scores)):
#     #print(str(list_of_all_scores[i]) + " " + str(list_of_all_similarities[i]))
#     outF.write(str(list_of_all_scores[i]).rstrip())
#     outF.write(" ")
#     outF.write(str(list_of_all_similarities[i]))
#     outF.write("\n")
# outF.close()        

list_sim_score = []
for k in range(len(listOfLists)):
    first_id = listOfLists[k][0]
    for l in range(len(listOfLists[k])):
        dict_of_sim_score = {}
        if(l!=0):
            dict_of_sim_score = {
                'q_id': first_id,
                't_id': listOfLists[k][l],
                'similarity': score_listOfLists[k][l-1],
                'score': list_of_all_scores[k][l-1]
            }
            list_sim_score.append(dict_of_sim_score)

outF = open("./data/GraphData.txt", "w")
for dic in list_sim_score:
    json.dump(dic, outF)
    outF.write("\n")

