ano = int(input('Ano? '))
if ano%100==0 and ano%400==0:
    print('Ano bissexto')
elif ano%4==0:
    print('Ano bissexto')
else:
    print('Ano não bissexto')