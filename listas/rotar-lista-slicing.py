# ##
# @file rotar-lista.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   7/febrero/2021
# @url  http://lineadecodigo.com/python/rotar-lista-con-slicing-en-python/
# @description Rota los elementos de una lista con slicing
# ##


#Definimos la lista
lista = [1,2,3,4,5,6,7,8,9]
print (lista)

# Rotar a derecha
lista = lista[3:]+lista[:3]
print (lista)

# Rotar a derechas
lista = lista[-6:]+lista[:-6]
print (lista)
