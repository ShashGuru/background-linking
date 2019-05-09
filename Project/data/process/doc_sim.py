import json
import collections
import spacy
nlp = spacy.load('en_core_web_md')

with open('data.json', 'r') as fp:
    data = json.load(fp)
doc_dict =collections.OrderedDict()
for k, v in data.items():
    v = v.replace("\xad","-")
    v = v.replace("\xa0"," ")
    v = v.replace("\u2009"," ")   
    doc_dict[k] = nlp(v)

query_id = "9171debc316e5e2782e0d2404ca7d09d"
query_file = open("query.txt", "r")
#print(query_file.read())
query_str = nlp(str(query_file.read()))

for k, v in doc_dict.items():   

    print( k + " : " + str(query_str.similarity(v)))