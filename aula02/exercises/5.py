price= float(input("Litros? "))

if price<40:
	preco= price*1.40
	
else:
	preco= price*1.4*0.90
	
print("O preço a pagar será:", preco, "€")
