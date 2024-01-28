# ##
# @file borrar-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/xxx/
# @description Borra un fichero
# ##

from os import remove, path

fichero = "fichero.txt"
if path.exists(fichero):
    remove(fichero)
    print("Fichero eliminado")
else:
    print("El fichero no existe")