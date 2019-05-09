import json
import operator
import pickle
query_file = open("./data/queries_attr_file.txt")

list_of_qry_js = []
for line1 in query_file:
    json_line = json.loads(line1)
    topics = json_line['topics']
    for k,v in topics.items():
        topics[k] = float(v)    
    list_of_qry_js.append(json_line)

target_file = open("./data/all_attr_new.txt")
list_of_target_js = []
for line1 in target_file:
    json_line = json.loads(line1)
    topics = json_line['topics']
    for k,v in topics.items():
        topics[k] = float(v)    
    list_of_target_js.append(json_line)   
    

#head_list = ['topic_score','similarity','news_type','date','author','size','score']

data_list = [[]]
#data_list.append(head_list)
for q_dict in list_of_qry_js:
    for t_dict in list_of_target_js:
        if q_dict['id'] == t_dict['q_id']:
            query_topics = q_dict['topics']
            target_topics = t_dict['topics']
            present = 0
            if (query_topics and target_topics):
                sorted_q = sorted(query_topics.items(), key=operator.itemgetter(1), reverse=True)[:3]
                sorted_t = sorted(target_topics.items(), key=operator.itemgetter(1), reverse=True)[:3]
                # sorted_q = sorted_query[:3]
                # sorted_t = sorted_target[:3]
                
                for dic_q in sorted_q:
                    for dic_t in sorted_t:
                        if dic_q[0] == dic_t[0]:
                            present = 1
                
                # for i in range(3):
                #     k_q = sorted_q[i][0]
                #     if k_q == sorted_t[i][0]:
                #         present = 1
            news_type = 1 if q_dict['news_type'] == t_dict['news_type'] else 0
            date = 1 if int(t_dict['date']) > int(q_dict['date']) else 0
            author = 1 if q_dict['author'] == t_dict['author'] else 0
            size  = 0
            if q_dict['size'] < t_dict['size']:
                size = 1
            tar_list = [present,float(t_dict['similarity']),news_type, date, author,size, int(t_dict['score']) ]
            data_list.append(tar_list)
data_list.pop(0)
with open("./results/output.txt","wb") as f:
    pickle.dump(data_list,f)