# ##
# @file añadir-contenido-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/xxx/
# @description Añade contenido a un fichero existente
# ##

from os import path

fichero = "fichero.txt"

if (path.exists(fichero)):
    with open(fichero,"a") as fichero:
        fichero.write("Fila añadida al Contenido del fichero\n")
else:
    print(f"El fichero {fichero} no existe")