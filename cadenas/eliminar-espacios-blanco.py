# ##
# @file eliminar-espacios-blanco.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   17/enero/2021
# @url  http://lineadecodigo.com/python/pdte/
# @description Elimina espacios en blanco de una cadena
# ##

cadena = ' \tSoy una cadena\t\n\tSoy una cadena tabulada \n Soy otra cadena'
print ("---Cadena Original---")
print (cadena)

print ("---Cadena con strip---")
cadena_uno = cadena.strip()
print (cadena_uno)

print ("---Cadena con .replace---")
cadena_dos = cadena.replace(" ","")
print (cadena_dos)

print ("---Cadena con join---")
cadena_tres = " ".join(cadena.split())
print (cadena_tres)