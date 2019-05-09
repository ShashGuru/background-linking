queryIdList = []
file = open("./data/bqrels.final.txt", "r")
for line in file:
    strList = line.split(' ')
    queryIdList.append(strList[2])
print(queryIdList)
