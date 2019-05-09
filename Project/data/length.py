import json_lines
import json
i=0

with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        i += 1
        #if i%1000 == 0:
    print(i)