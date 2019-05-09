import tm3
import json
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

file1 = open("./data/GraphData_short.txt", "r")
file2 = open("./results/all_attr_file.txt","w+")
#list_of_atts = []
count_docs = 0
for line in file1:
    line = line.replace("\\n",'')
    ln = json.loads(line)
    id = ln['t_id']
    
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
    paragraph = list_of_docs['_source']['paragraph']
    ln['news_type'] = list_of_docs['_source']['news_type']
    ln['title'] = list_of_docs['_source']['title']
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
    if(count_docs%85==0):
        print(count_docs/85)
    count_docs+=1

file1.close()
file2.close()
    

