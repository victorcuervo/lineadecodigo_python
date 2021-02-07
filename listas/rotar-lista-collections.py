# ##
# @file rotar-lista.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   7/febrero/2021
# @url  http://lineadecodigo.com/python/pdte/
# @description Rota los elementos de una lista con librería collections y el obejto deque
# ##

from collections import deque

#Definimos la lista
lista = [1,2,3,4,5,6,7,8,9]
print (lista)

# Rotar a derecha
lista = deque(lista)
lista.rotate(3)
print (list(lista))

# Rotar a derechas
lista.rotate(-6)
print (list(lista))
