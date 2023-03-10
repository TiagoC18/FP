#O código abaixo lida com comboios de mercadorias. Cada comboio é representado por uma lista de vagões e cada vagão é uma lista com o
#tipo e a quantidade de mercadoria que transporta. Por exemplo,
t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
#representa um comboio com 5 vagões: o primeiro vagão tem 30 toneladas de carvão, o segundo tem 50 toneladas de arroz, etc.
#Complete a função cargoQuantity(t, m) para devolver a quantidade total de mercadoria do tipo m contida no comboio t. Por exemplo,
#cargoQuantity(t, 'rice') deve devolver 92.

#trains.py
# Constantes para indexar os vagões:
M, Q = 0,1
# Se w=['coal', 45), então w[M]='coal' e w[Q]=45.

def cargoQuantity(t, m) :
    #Quantidade total de mercadoria de tipo m no comboio t.
    val= 0
    for i in t:
        if i[0] == m:
            val+= i[1]
    return val

def unload(t, m, q):
    #Descarrega quantidade q da mercadoria do tipo m
    val= cargoQuantity(t,m)
    if val<q:
        for i in range(len(t)-1,-1,-1):
            if t[i][0]==m:
                t.pop(i)
    return q-val


print("Coal:", cargoQuantity(t,"coal"))
print("Rice:", cargoQuantity(t,"rice"))