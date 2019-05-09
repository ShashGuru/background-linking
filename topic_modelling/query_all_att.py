import tm3
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()
import json

queryIdList = []

f = open("./data/newsir18-background-linking-topics.v2.xml", "r")
i= 0
for x in f:
  if (i-2)%6 == 0:
      listOfIds = x.split(' ')
      queryIdList.append(listOfIds[1])
  i+=1
file2 = open("./results/queries_attr_file.txt","w+")
count_docs = 0
for id in queryIdList:
    ln = {}
    query = {
        "_source": ["paragraph","news_type",'title','author','date'],
        "size" : 10000,
        "query": {
            "ids" : {
                "type" : "news_articles",
                "values" : id
            }
        }
    }
    res = es.search(index="trec_news", body=query)
    list_of_docs = res['hits']['hits'][0]
    ln['id'] = id
    paragraph = list_of_docs['_source']['paragraph']
    ln['size'] = len(paragraph)
    ln['news_type'] = list_of_docs['_source']['news_type']
    title_str = list_of_docs['_source']['title']
    title_str = title_str.replace('\'', '')
    title_str = title_str.replace('\"','')
    title_str = title_str.replace("\xad","-")
    title_str = title_str.replace("\xa0"," ")
    title_str = title_str.replace("\u2014","-")
    title_str = title_str.replace("\u2018","")
    title_str = title_str.replace("\u2019","")
    title_str = title_str.replace("\u2019s","")    
    title_str = title_str.replace("\u2009"," ")
    ln['title'] = title_str
    ln['author'] = list_of_docs['_source']['author']
    ln['date'] = list_of_docs['_source']['date']
    dict_of_topics = {}
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
            score = str2[0]
            dict_of_topics[topic] = score           
    ln['topics']= dict_of_topics
    file2.write(json.dumps(ln) + "\n")
    #list_of_atts.append(ln)
    if(count_docs%0.5==0):
        print(count_docs/0.5)
    count_docs+=1

file2.close()