from elasticsearch import Elasticsearch
es = Elasticsearch()

res = es.get(index="trec_news", doc_type='news_articles', id='00f57310e5c8ec7833d6756ba637332e')
print(res['_source'])