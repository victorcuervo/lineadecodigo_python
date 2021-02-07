# ##
# @file eliminar-elemento-listapy
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   7/febrero/2021
# @url  http://lineadecodigo.com/python/pdte/
# @description Elimina un elemento de una lista
# ##


# Codigo que nos permite add un elemento a una lista

lista = [1,4,3,4,5]

for elemento in lista:
    print (elemento)

# Borramos el 4. El primero que encuentre
lista.remove(4)

for elemento in lista:
    print (elemento)


# Borramos la posición 4
lista = [1,4,3,4,5]
lista.pop(4)

for elemento in lista:
    print (elemento)


# Borramos la posición 4
lista = [1,4,3,4,5]
del lista[4]

for elemento in lista:
    print (elemento)


