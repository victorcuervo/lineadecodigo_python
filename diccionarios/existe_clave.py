# coding: utf8
# ##
# @file existe_clave.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   3/julio/2017
# @url  http://lineadecodigo.com/python/comprobar-claves-diccionario-python/
# @description Comprobar que un diccionario de Python tiene una clave
# ##

colores = {'rojo':'red','azul':'blue','verde':'green'}

print colores['rojo']

if 'amarillo' in colores:
    print colores['amarillo']
else:
    print 'No hay traducción para el color amarillo'