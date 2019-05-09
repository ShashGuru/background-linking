from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.get(index="trec_news", doc_type='news_articles', id='GUZ3H2oB7Pm8G7qmpjwM')
print(res['_source'])