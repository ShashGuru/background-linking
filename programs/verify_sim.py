import json
from gensim.models.keyedvectors import KeyedVectors
from DocSim import DocSim
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

googlenews_model_path = './data/GoogleNews-vectors-negative300.bin'
stopwords_path = "./data/stopwords_en.txt"

model = KeyedVectors.load_word2vec_format(googlenews_model_path, binary=True)
with open(stopwords_path, 'r') as fh:
    stopwords = fh.read().split(",")
ds = DocSim(model,stopwords=stopwords)

q1 = '9171debc316e5e2782e0d2404ca7d09d'
q2 = '2a340b8573d498e261d6f2365b37f8eb'
q3 = '7ef8ce1720bf2f6b2065a97506ee89b4'
q4 = 'c3cea789141ef2ae856419e86e165e0c'


