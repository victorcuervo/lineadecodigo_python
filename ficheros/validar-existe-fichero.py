# ##
# @file validar-existe-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/xxx/
# @description Valida que exista un fichero
# ##

from os import path

fichero = "fichero.txt"

if (path.exists(fichero)):
    print(f"Existe el fichero {fichero}")
else:
    print(f"No existe el fichero {fichero}")