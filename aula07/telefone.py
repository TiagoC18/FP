# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    matches = {}
    for num, name in contacts.items():
        if partName.lower() in name.lower():
            matches[num] = name
    return matches

def addContact(contacts):
    num= input("Number:")
    if num in contacts:
        print ("Este número já se encontra na sua lista de contactos")
    
    name= input("Nome:")
    contacts[num]= name

def removeContact(contacts):
    num= input("Number:")
    if num in contacts:
        input("Pretende eliminar o número {} : {} ? Se sim premir S".format(num, contacts[num])).upper()
        if input == "S":
            contacts.pop(num)
    else:        
        print("Este número não existe na sua lista de contactos")
    return contacts

def searchNumber(contacts):
    num= input("Introduzir número:")
    if num in contacts:
        print(contacts.get(num, num))
    else:
        print("Não tem este número inserido nos seus contactos")


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("Escreva o número e respetivo nome que pretende adicionar")
            addContact(contactos)
        elif op == "R":
            removeContact(contactos)
        elif op == "L":
            searchNumber(contactos)
        elif op == "P":
            partName= input("Escrever a parte do nome:")
            if partName == "":
                print("Não foi nada escrito")
            else:
                print()
                print("Correspondências:")
                listContacts(filterPartName(contactos, partName))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

