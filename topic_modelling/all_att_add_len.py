import tm3
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()
import json

queryIdList = []
count_docs = 0
file1 = open("./results/all_attr_new.txt",'w')
f = open("./results/all_attr_file.txt", "r")
for line in f:
    ln = json.loads(line)
    id = ln['t_id']
    title_str = ln['title']
    if title_str is not None:
        title_str = title_str.replace('\'', '')
        title_str = title_str.replace('\"','')
        title_str = title_str.replace("\xad","-")
        title_str = title_str.replace("\xa0"," ")
        title_str = title_str.replace("\u2014","-")
        title_str = title_str.replace("\u2018","")
        title_str = title_str.replace("\u2019","")
        title_str = title_str.replace("\u2019s","")    
        title_str = title_str.replace("\u2009"," ")
        #title_str = title_str.replace(' ','')
    ln['title'] = title_str
    query = {
        "_source": ["paragraph"],
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
    paragraph = list_of_docs['_source']['paragraph']
    ln['size'] = len(paragraph)
    file1.write(json.dumps(ln) + "\n")
    #list_of_atts.append(ln)
    if(count_docs%85==0):
        print(count_docs/85)
    count_docs+=1

file1.close()
f.close()