import tm3
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

queryIdList = []
file = open("./data/bqrels.final.txt", "r")
for line in file:
    strList = line.split(' ')
    queryIdList.append(strList[2])

f = open("./data/newsir18-background-linking-topics.v2.xml", "r")
i= 0
for x in f:
  if (i-2)%6 == 0:
      listOfIds = x.split(' ')
      queryIdList.append(listOfIds[1])
  i+=1

#all_16_list = ['9171debc316e5e2782e0d2404ca7d09d','00f57310e5c8ec7833d6756ba637332e','035622671d5ee6a098d686c9a4d5b18e','071ad6f3cfba2273c7f8d5264c0a7583','0da8ee91889db59cd8d8c4437655a0ef','1b946cdcd37c1a398cdd08d88111add4']

list_in_use = queryIdList

query = {
    "_source": ["paragraph"],
    "size" : 10000,
    "query": {
        "ids" : {
            "type" : "news_articles",
            "values" : list_in_use
        }
    }
}




res = es.search(index="trec_news", body=query, scroll='10m')
dict_of_docs = res['hits']['hits']

file1 = open("top_file.txt","w+")
count_docs = 0
for doc in dict_of_docs:
    id = doc['_id']
    #if id == list_in_use[0]:
        #print("main id")
    #dict_of_topics = {}
    paragraph = doc['_source']['paragraph']
    if paragraph != '' and len(paragraph)>20:
        topics = tm3.comp_topics([paragraph])
        top_str = topics[0][1]
        top_str = top_str.replace('\'', '')
        top_str = top_str.replace('\"','')
        top_str = top_str.replace(' ','')
        str1 = top_str.split("+")
        for strs in str1:
            str2 = strs.split("*")
            topic = str2[1]
            #score = str2[0]
            #dict_of_topics[topic] = score
            file1.write(topic + " ")
        #print(dict_of_topics) 
    if(count_docs%85==0):
        print(count_docs/85)
    count_docs+=1
file1.close()       
    
