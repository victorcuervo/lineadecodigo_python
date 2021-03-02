# ##
# @file eliminar-elemento-listapy
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   7/febrero/2021
# @url  http://lineadecodigo.com/python/eliminar-elementos-duplicados-de-una-lista-con-python/
# @description Elimina los elementos duplicados de una lista
# ##


# Codigo que nos permite add un elemento a una lista

lista = [1,4,3,4,5,1,2,8,7,4,3,1,3]
print (lista)

# Al crear un diccionario elimina los duplicados
lista = list(dict.fromkeys(lista))
print (lista)
