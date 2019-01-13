lista=[10, 20, 30]
def rekuprint(lista):
    if len(lista)==1:
        print(lista[0])
    else:
        print(lista[0])
        rekuprint(lista[1:])
rekuprint(lista)