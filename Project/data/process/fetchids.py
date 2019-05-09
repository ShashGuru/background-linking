f = open("newsir18-background-linking-topics.v2.xml", "r")
i= 0
for x in f:
  if (i-2)%6 == 0:
      listOfIds = x.split(' ')
      print(listOfIds[1])
  i+=1