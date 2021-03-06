from gensim.models.keyedvectors import KeyedVectors
from DocSim import DocSim
import json
import collections

googlenews_model_path = './data/GoogleNews-vectors-negative300.bin'
stopwords_path = "./data/stopwords_en.txt"



with open('data.json', 'r') as fp:
    data = json.load(fp)
doc_list = []
for k, v in data.items():
    if k == '56f0438ee0fb34c341ccf5af36de5175':
        query_str = v
        #print("query " +v)
    else:    
        v = v.replace("\xad","-")
        v = v.replace("\xa0"," ")
        v = v.replace("\u2009"," ")   
        doc_list.append(v)
        #print("target " + v)

#query_id = "9171debc316e5e2782e0d2404ca7d09d"
#query_file = open("query.txt", "r")
#print(query_file.read())
#query_str = query_file.read()
model = KeyedVectors.load_word2vec_format(googlenews_model_path, binary=True)
with open(stopwords_path, 'r') as fh:
    stopwords = fh.read().split(",")
ds = DocSim(model,stopwords=stopwords)
sim_scores = ds.calculate_similarity(query_str, doc_list)


for j in sim_scores:
    print(j['score'])

# Prints:
##   [ {'score': 0.99999994, 'doc': 'delete a invoice'}, 
##   {'score': 0.79869318, 'doc': 'how do i remove an invoice'}, 
##   {'score': 0.71488398, 'doc': 'purge an invoice'} ]