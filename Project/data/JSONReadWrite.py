import json_lines
import json
import re
line_count=0
with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        if line_count < 386088: 
            if line_count == 386087:
                id = item['id']
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
                            paragraph.strip()
                    i+=1
                print(paragraph)   
            line_count += 1
        else:
            exit()