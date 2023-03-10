a1= float(input('a1? '))
b1= float(input('b1? '))
a2= float(input('a2? '))
b2= float(input('b2? '))

if a1<a2<b1 or a1<b2<b1 or a2<b1<b2 or a2<a1<b2:
    print("True")
else:
    print("False")