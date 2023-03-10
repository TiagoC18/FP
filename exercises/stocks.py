#1
#A função main define uma lista de tuplos com informação sobre acções de diversas empresas transacionadas em bolsas de várias cidades.
#Cada tuplo contém os campos: empresa, cidade, preço-de-abertura, preço-de-fecho, volume.
#Defina uma função printStocks (stocks) para mostrar a tabela com as colunas formatadas como no exemplo abaixo. Inclua uma coluna com a valorização da ação em percentagem.
#Por exemplo, se o preço de abertura for 10.00 e o de fecho for 9.50, a valorização será de -5%
#Note que esta função é chamada pela função main e não deve modificar a lista passada no argumento.

#from util import *

from random import random
stocks = [ ('INTC', 'London', 34.249, 34.451, 1792860),
            ('TSLA', 'London', 221.33, 229.63, 398520),
            ('EA', 'Paris', 72.63, 68.98, 1189510),
            ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
            ('TSLA', 'Paris', 217.35, 217.75, 252500),
            ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
        ]

lst=[]
for i in stocks:
    lst.append([i[0], i[4]])
print (lst)

def printStocks(stocks):
     for i in stocks:
        f= i[3]
        a= i[2]
        if f>a:
            val= -(1-(a/f))
        else:
            val= 1-(f/a)
        
        print("{:<10} {:<10} {:^10.2f} {:>10.2f} {:>10} {:<3.0}%".format(i[0], i[1], i[2], i[3], i[4], val*100))
    
    
#def main():
# Cada tuplo = (empresa, cidade, abertura, fecho, volume)
printStocks(stocks)


#Acrescente os argumentos adequados à função sorted para obter uma tabela ordenada alfabeticamente pelo nome da empresa e, para a
#mesma empresa, por ordem decrescente do volume transacionado.
#stocks.py
#from util import *

# Cada tuplo = (empresa, cidade, abertura, fecho, volume)
def main():

    print("----")
    # Complete...
    stocks2 = sorted(stocks, key= lambda t: (t[0], t[4]), reverse=True)
    for i in stocks2:
        print("{:<10} {:<10} {:^10.2f} {:>10.2f} {:>10}".format(i[0], i[1], i[2], i[3], i[4]))


if __name__ == "__main__":
    main()
