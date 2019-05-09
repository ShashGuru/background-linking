import json_lines
import json
import tm3
import sys, traceback
import re
from datetime import datetime
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()
doc_count = 0
docs=[]
print(datetime.now().strftime('%H:%M:%S'))
try: 
    with open("D:\\Course_Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
        for item in json_lines.reader(f):
            news_id = item['id']
            url=item['article_url']
            title=item['title']
            if title is not None:
                title = title.replace('\'', '')
                title = title.replace('\"','')
                title = title.replace("\xad","-")
                title = title.replace("\xa0"," ")
                title = title.replace("\u2014","-")
                title = title.replace("\u2018","")
                title = title.replace("\u2019","")
                title = title.replace("\u2019s","")    
                title = title.replace("\u2009"," ")
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
            if paragraph is not None:
                paragraph = paragraph.replace('\'', '')
                paragraph = paragraph.replace('\"','')
                paragraph = paragraph.replace("\xad","-")
                paragraph = paragraph.replace("\xa0"," ")
                paragraph = paragraph.replace("\u2014","-")
                paragraph = paragraph.replace("\u2018","")
                paragraph = paragraph.replace("\u2019","")
                paragraph = paragraph.replace("\u2019s","")    
                paragraph = paragraph.replace("\u2009"," ") 
            size = len(paragraph) 

            dict_of_topics = {}
            if paragraph is not None and len(paragraph)>20:
                topics = tm3.comp_topics([paragraph])
                top_str = topics[0][1]
                top_str = top_str.replace('\'', '')
                top_str = top_str.replace('\"','')
                top_str = top_str.replace(' ','')
                str1 = top_str.split("+")
                for strs in str1:
                    str2 = strs.split("*")
                    topic = str2[1]
                    score = str2[0]
                    dict_of_topics[topic] = score           
            topics1 = json.dumps(dict_of_topics)
            doc = {
                'url': url,
                'title': title,
                'author': author,
                'date': date,
                'news_type': news_type,
                'paragraph': paragraph,
                'size': size,
                'topics': topics1
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