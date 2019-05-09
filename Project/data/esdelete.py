from elasticsearch import Elasticsearch
es = Elasticsearch()

es.indices.delete(index='trec_news',ignore=[400, 404])