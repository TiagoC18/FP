Seg= int(input('Segundos? '))

h= Seg//3600
m=(Seg%3600)//60
s= (((Seg%3600)%60)%60)

print("{:02d}:{:02d}:{:02d}".format(h, m, s))