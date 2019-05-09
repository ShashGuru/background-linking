import collections
def func_num_id():
    f = open("./data/newsir18-background-linking-topics.v2.xml", "r")
    j= 0
    listOfIds = []
    listOfNums = []
    for x in f:
        if (j-1)%6 == 0:
            listOfNums_1 = x.split(' ')
            listOfNums.append(listOfNums_1[2]) 
        if (j-2)%6 == 0:
            listOfIds_1 = x.split(' ')
            listOfIds.append(listOfIds_1[1])
        j+=1

    dict_num_id = collections.OrderedDict()
    i = 0
    for i in range(len(listOfIds)):
        dict_num_id[listOfNums[i]] = listOfIds[i]

    return dict_num_id