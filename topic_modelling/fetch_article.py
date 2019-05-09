from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

list_in_use = '049739753ce2e539d8dc2165daaf6aa6'
query = {
    "_source": ["paragraph","news_type",'title'],
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

f = open("./results/p4.txt","w")
f.write(list_in_use + "--")
for doc in dict_of_docs:
    title = doc['_source']['title']
    news_type = doc['_source']['news_type']
    paragraph = doc['_source']['paragraph']
    f.write(str(title) + "--")
    f.write(news_type + " ---")
    f.write(paragraph)
f.close()    
