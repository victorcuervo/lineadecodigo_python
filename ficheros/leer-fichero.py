# ##
# @file leer-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/xxx/
# @description Lee el contenido de un fichero de golpe y línea a línea
# ##

from os import path

nombre_fichero = "fichero.txt"

if (path.exists(nombre_fichero)):
    with open(nombre_fichero,"r") as fichero:
        print(fichero.read())

    with open(nombre_fichero,"r") as fichero:
        for line in fichero:
            print(line)
else:
    print(f"El fichero {nombre_fichero} no existe")






