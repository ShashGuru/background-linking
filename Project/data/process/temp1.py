dict1 = {'a1c41a70-35c7-11e3-8a0e-4e2cf80831fc': ' The “now hiring” sign', 'abc':'efg'}
f = open("dict.txt","w")
for k, v in dict1.items():
    f.write(k + ':'+ v + '\n')
f.close()  