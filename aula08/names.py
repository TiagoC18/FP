
with open("names.txt") as names:
        dic={}

        names.readline()
        for line in names:
            name= line.strip().split()
            last= name[-1]
            first= name[0]
            
            dic[last]= dic.get(last, [])
            dic[last].append(first)
for e in dic:
    print(e, ":", dic[e])      
   


