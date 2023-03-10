def inputFloatList():
    lst=[]
    a= input("Introduzir número:")
    while a!="":
        lst.append(float(a))
        a= input("Introduzir número:")
    return lst



def countLower(lst, v):
    lst= inputFloatList()
    c=0
    for lst.count in len(lst):
        if len(lst) <v:
            c=c+1
    return c


def minmax():
    lst= inputFloatList()
    lst2= sorted(lst)
    min= lst2[0]
    max= lst2[-1]
    return min, max