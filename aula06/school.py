# Complete o programa!
from os import name
from tkinter import filedialog
# a)
def loadFile(fname1, lst):
    with open (fname1) as values:
        

    
# b) Crie a função notaFinal aqui...
...

# c) Crie a função printPauta aqui...
...

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


