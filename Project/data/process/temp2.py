import json_lines
import re
import json
doc_count=0
ignoreDocs = ['opinion','letters to the editor','the post\'s view','the posts view']
with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        contents = item['contents']
        if 'kicker' in contents[1]:
            if str(contents[1]['kicker']).lower() in ignoreDocs:
                print(contents[1]['kicker'])
        if doc_count%6000 == 0:
            print(doc_count/6000)    
        doc_count+=1 
