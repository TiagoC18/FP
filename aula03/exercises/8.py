print("primeiraa resolução:")

a1 = float(input("valor de a1: "))
b1 = float(input("valor de b1: "))
a2 = float(input("valor de a2: "))
b2 = float(input("valor de b2: "))


def interset(a1, b1, a2, b2):
	if a1 >= b1 or a2 >= b2:
		x = print ("erro")
	elif (a1 < a2 < b1) or (a1 < b2 < b1) :
		x = print ("True - há interseção")
	else:
		x = print ("False - não há interseção")
	return x
	
x = interset(a1, b1, a2, b2)

print("segunda resolução:")

a1 = float(input("valor de a1: "))
b1 = float(input("valor de b1: "))
a2 = float(input("valor de a2: "))
b2 = float(input("valor de b2: "))


def interset(a1, b1, a2, b2):
	if a1 >= b1 or a2 >= b2:
		return "erro"
	elif (a1 < a2 < b1) or (a1 < b2 < b1) :
		return "interseta"
	else:
		return "não interseta"
	
print("o intervalo [", a1, ",", b1, "] ", interset(a1, b1, a2, b2), " o intervalo [", a2, ",", b2, "]", sep='')
