print("primeira resolução:")

def p(x):
	f = (x**2) + 2*x + 3
	return f
	
x = int(input("valor de x: "))
f = p(x)

def r(x):
	q = (p(x)**2) + 2 * p(x) +3
	return q

q = r(x)

if f ==6:
	print("Para x =" , x, " o valor de p(", x,") é ", f, sep='')
	print("Para x =" , x, " o valor de p(p(", x, ")) é ", q, sep='')	
else:
	print("Para x =" , x, " o valor de p(", x,") é ", f, sep='')
	
#or

print("segunda resolução:")

def p(x):
	result = x**2+2*x+3
	return result
	
print ("p(0) = ", p(0))
print ("p(1) = ", p(1))
print ("p(2) = ", p(2))
print ("p(p(1)) = ", p(p(1)))