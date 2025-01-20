# ##
# @file validar-existe-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  https://lineadecodigo.com/python/comprobar-que-existe-un-fichero-en-python/
# @description Valida que exista un fichero
# ##

from os import path

fichero = "fichero.txt"

if (path.exists(fichero)):
    print(f"Existe el fichero {fichero}")
else:
    print(f"No existe el fichero {fichero}")