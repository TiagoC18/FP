n= int(input("Número de termos da série:"))
pi= ((-1)**n)/(2*n+1)
while n>=0:
    pi= pi+(((-1)**n)/(2*n+1))
    n-=1
    
print("A soma dos n primeiros termos desta série é:", pi)