import tm3
from elasticsearch import Elasticsearch,helpers
es = Elasticsearch()

all_16_list = ['9171debc316e5e2782e0d2404ca7d09d','00f57310e5c8ec7833d6756ba637332e','035622671d5ee6a098d686c9a4d5b18e','071ad6f3cfba2273c7f8d5264c0a7583','0da8ee91889db59cd8d8c4437655a0ef','1b946cdcd37c1a398cdd08d88111add4']
all_8_list = ['9171debc316e5e2782e0d2404ca7d09d','09b3167f0d1aa5cfa8be932bb704d75a','0a378bae-7833-11e1-b191-2d5f686e7ff4','0caa33d172c696cac4bbc36df4e44bf2','0e92c3bb3dbf2dc654a2a854752651ce','12089ed7089574776db6c1e5e55704af','13f8aae591e8e04da2ef606c65290cb2']
all_4_list = ['9171debc316e5e2782e0d2404ca7d09d','049739753ce2e539d8dc2165daaf6aa6','13381e831a417a6db347ec237373d3ff','139c0f1649fa758d2379555c91b9c37e','154f5bda366134a3b74e60c0611b20b0','191467c688f6355aa1e36f6f2e5543af']
all_2_list = ['9171debc316e5e2782e0d2404ca7d09d','02ae7136-006d-11e3-9711-3708310f6f4d','071068774e4eb454c1702192fcca886b','0bca80bf2a80b62a0e216540861ef7a9','1114e343-d128-4a7d-bb5d-66d2a9836f72','2e084bb1a85b8520fa17345f29bdb1c8']
all_0_list = ['9171debc316e5e2782e0d2404ca7d09d','041e530b21766fc294d4e9c48b1e2723','07578ec30a042be5678bda5f99949ff3','4a7c2970fd9bf65fe09c7cf46df7b06d','8c9449b32ddf6b1ca349b58eb2edf401','9171debc316e5e2782e0d2404ca7d09d']

list_in_use = all_16_list

query = {
    "_source": ["paragraph"],
    "size" : 10000,
    "query": {
        "ids" : {
            "type" : "news_articles",
            "values" : list_in_use
        }
    }
}




res = es.search(index="trec_news", body=query, scroll='10m')
dict_of_docs = res['hits']['hits']

for doc in dict_of_docs:
    id = doc['_id']
    if id == list_in_use[0]:
        print("main id")
    dict_of_topics = {}
    paragraph = doc['_source']['paragraph']
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
    print(dict_of_topics)    
    
