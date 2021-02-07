#Codigo para recorrer listas de forma recursiva

def listar (lista):
    for n in lista:
        if isinstance(n,list):
            listar(n)
        else:
            print (n)

lista = [1,2,3,['a','b','c','d'],4,5]
listar(lista)
