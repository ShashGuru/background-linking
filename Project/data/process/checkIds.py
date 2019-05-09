import json_lines
import re
doc_count=0
dictOfDocs = {}
listOfIds = ['049739753ce2e539d8dc2165daaf6aa6','02ae7136-006d-11e3-9711-3708310f6f4d']
with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        id = 0
        id = item['id']
        if id in listOfIds:
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
            #print(paragraph)
            dictOfDocs.update({id : paragraph})
        if doc_count%6000 == 0:
            print(doc_count/6000)
        doc_count+=1
f = open("dict.txt","w", encoding="utf-8")
printcount = 0
for k, v in dictOfDocs.items():
    printcount+=1
    f.write(v)
    print(printcount)
f.close() 
