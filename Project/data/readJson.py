import json
import re

f=open("output2.txt","r")
jsonString = f.read()

jsonDict = json.loads(jsonString)

id = jsonDict['id']
url=jsonDict['article_url']
title=jsonDict['title']
author=jsonDict['author']
date=jsonDict['published_date']
contents = jsonDict['contents']
news_type = contents[0]['content']
paragraph=""
i=0
TAG_RE = re.compile(r'<[^>]+>')
while i<len(contents):
    if  'subtype' in contents[i] and contents[i]['subtype'] == 'paragraph':
        str = TAG_RE.sub('', contents[i]['content'])
        paragraph+=" "
        paragraph+=str
    i+=1

print(paragraph)        

