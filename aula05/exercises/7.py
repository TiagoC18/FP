s= str(input("Nome:"))
def shorten(s):
    list(s)
    name=""
    for a in s:
        if a.isupper():
            name= name + a
    return name
shorten(s)