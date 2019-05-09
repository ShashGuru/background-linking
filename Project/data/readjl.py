import json_lines
import json
i=0
f2= open("output386087.txt","w+")
with open("D:\\Course Content\\Thesis\\WashingtonPost.v2.tar\\WashingtonPost.v2\\data\\TREC_Washington_Post_collection.v2.jl", 'rb') as f:
    for item in json_lines.reader(f):
        if i < 386088:
            if i == 386087:
                json2 = json.dumps(item)
                f2.write(json2)
            i += 1
        else:
            f2.close()
            exit()    