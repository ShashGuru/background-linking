import json_lines
import json
import sys, traceback
import re
from datetime import datetime
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()
doc_count = 0
docs=[]
print(datetime.now().strftime('%H:%M:%S'))
try: 
    with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
        for item in json_lines.reader(f):
            news_id = item['id']
            url=item['article_url']
            title=item['title']
            author=item['author']
            date=item['published_date']
            contents = item['contents']
            if 'content' in contents[0] and contents[0]['type'] == 'kicker':
                news_type = contents[0]['content']
            else:
                news_type=""
            i=0
            paragraph=""
            TAG_RE = re.compile(r'<[^>]+>')
            while i<len(contents):
                if(contents[i] is not None):
                    if  'subtype' in contents[i] and contents[i]['subtype'] == 'paragraph':
                        str = TAG_RE.sub('', contents[i]['content'])
                        paragraph+=" "
                        paragraph+=str
                i+=1
            paragraph = paragraph.replace("\xad","-")
            paragraph = paragraph.replace("\xa0"," ")
            paragraph = paragraph.replace("\u2009"," ")     
            doc = {
                'url': url,
                'title': title,
                'author': author,
                'date': date,
                'news_type': news_type,
                'paragraph': paragraph
            } 
            #docs.append(doc)
            es.index(index="trec_news", doc_type='news_articles', id=news_id,  body=doc)
            if doc_count%6000 == 0:
                print(doc_count/6000)
            doc_count+=1   
    #helpers.bulk(es, actions=docs, index="trec_news", doc_type='news_articles') 
   
    es.indices.refresh(index="trec_news")
    res = es.search(index="trec_news", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    print(len(res))
    print(datetime.now().strftime('%H:%M:%S'))
except Exception as e:
    traceback.print_exc(file=sys.stdout)            
    print(doc_count)