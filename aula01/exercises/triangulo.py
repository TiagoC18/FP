import math
A= float(input('CatetoA:'))
B=float(input('CatetoB:'))
C= math.sqrt(A**2+B**2)
print('Hipotenusa', C)

aB= float(input('anguloB:'))

aA=180-90-aB
print('Ângulo entre o lado A e a hipotenusa:', aA)