# f = open("newsir18-background-linking-topics.v2.xml", "r")
# j= 0
# for x in f:
#   if (j-2)%6 == 0:
#       listOfIds_1 = x.split(' ')
#       listOfIds = listOfIds_1[1]
#   j+=1

#listOfIds = ['041e530b21766fc294d4e9c48b1e2723','02ae7136-006d-11e3-9711-3708310f6f4d','049739753ce2e539d8dc2165daaf6aa6','09b3167f0d1aa5cfa8be932bb704d75a','00f57310e5c8ec7833d6756ba637332e']
#listOfIds = ['7ef8ce1720bf2f6b2065a97506ee89b4','005308753e2d6f8a71c8be31be210e28','22e97660-300e-11e2-af17-67abba0676e2','07a71cda-2a58-11e5-bd33-395c05608059','0ad0297b51760f715083385fde0e0ef2','27b173ebedcfed892cdbc8dfbfbb1cfa']
listOfIds = ['c3cea789141ef2ae856419e86e165e0c','0395500d4733403755628be6858a9822','4555e8a6-e5a2-11e2-aef3-339619eab080','3c483e41871eb1f4dacb7baa0f7ca635','6f292ea0-796b-11e4-9721-80b3d95a28a9','6c9f3fc8-a0ba-11e4-b146-577832eafcb4']

import json_lines
import re
import json
doc_count=0
dictOfDocs = {}
with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        id = item['id']
        if id in listOfIds:
            print(id)
        #   if id == "9171debc316e5e2782e0d2404ca7d09d":
            contents = item['contents']
            i=0
            paragraph=""
            TAG_RE = re.compile(r'<[^>]+>')
            while i<len(contents):
                if(contents[i] is not None):
                    if  'subtype' in contents[i] and contents[i]['subtype'] == 'paragraph':
                        str = TAG_RE.sub('', contents[i]['content'])
                        paragraph+=" "
                        paragraph+=str
                        paragraph.strip()
                i+=1
                #paragraph2 = paragraph
            #print(paragraph) 
            dictOfDocs.update({id : paragraph})
            
        if doc_count%6000 == 0:
            print(doc_count/6000)
        doc_count+=1
# print()
# print(dictOfDocs)        
#f = open("dict.txt","w", encoding="utf-8")
# printcount = 0
# for k, v in dictOfDocs.items():
#     printcount+=1
#     f.write(k + ':'+ v + '\n')
#     print(printcount)
# f.close()     
with open('data.json', 'w') as fp:
    json.dump(dictOfDocs, fp) 