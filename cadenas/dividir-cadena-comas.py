# ##
# @file dividir-cadena-comas.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   17/enero/2021
# @url  http://lineadecodigo.com/python/pdte/
# @description Divide una cadena por un separador y la recorre
# ##

lista = "avión, coche, motocicleta, barco, submarino"
palabras = lista.split()

for palabra in palabras:
    print (palabra.strip())

palabras = lista.split(",")
for palabra in palabras:
    print (palabra.strip())