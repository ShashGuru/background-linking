import collections
def func_id_rank():
    listOfNums = []
    dict_num = collections.OrderedDict()
    f = open("./data/bqrels.final.txt", "r")
    for line in f:
        strs = line.split(' ')
        num = strs[0]
        id = strs[2]
        score = strs[3]
        
        if num not in listOfNums:
            listOfNums.append(num)
        
            dict_num[num] = []

        dic_id_score = {}
        dic_id_score[id] = score
        dict_num[num].append(dic_id_score)

    return dict_num