#O código abaixo lida com comboios de mercadorias. Cada comboio é representado por uma lista de vagões e cada vagão é uma lista com o
#tipo e a quantidade de mercadoria que transporta. Por exemplo,
from audioop import reverse


t =[['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
#representa um comboio com 5 vagões: o primeiro vagão tem 30 toneladas de carvão, o segundo tem 50 toneladas de arroz, etc.
#Complete a função unload(t, m, q), que deve descarregar do comboio t uma quantidade q de mercadoria de tipo m. Para isso, deve
#percorrer os vagões um a um, a partir do último, e descarregar total ou parcialmente os que tiverem a mercadoria pretendida até perfazer a
#quantidade pedida. Os vagões totalmente descarregados devem ser retirados do comboio, mas os restantes têm de ficar no comboio pela
#ordem original. Se conseguir descarregar toda a quantidade pedida, a função deve terminar e devolver zero. Se não, deve devolver a
#quantidade que ainda falta descarregar.

# Constantes para indexar os vagões:
M, Q =0 , 1
 # Se w['coal', 45], então w[M]='coal' e W[Q]=45.

def unload(t, m, q):
    #Descarrega quantidade q da mercadoria do tipo m
    val=0
    t.reverse()
    for i in t:
        

    #for i in t:
     #   if i == m:
      #      if q<t[Q]:

