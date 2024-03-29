# ##
# @file eliminar-elemento-listapy
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   7/febrero/2021
# @url  http://lineadecodigo.com/python/eliminar-elementos-de-una-lista-con-python/
# @description Elimina un elemento de una lista
# ##


# Codigo que nos permite add un elemento a una lista

lista = [1,4,3,4,5]

print ("Lista Inicial")
for elemento in lista:
    print (elemento)

print ("Método Remove")
# Borramos el 4. El primero que encuentre
lista.remove(4)

for elemento in lista:
    print (elemento)

print ("Método pop")
# Borramos la posición 4
lista = [1,4,3,4,5]
lista.pop(4)

for elemento in lista:
    print (elemento)

print ("Sentencia del")
# Borramos la posición 4
lista = [1,4,3,4,5]
del lista[4]

for elemento in lista:
    print (elemento)


