telList = ['975318642', '234000111', '777888333'] 
nameList = ['Angelina', 'Brad', 'Claudia']
def telToName(number):
    for i in telList:
        if telList[i]==number:
            return telList[i]
        else:
            return number

    