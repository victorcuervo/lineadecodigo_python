# ##
# @file listar-directorio.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/xxx/
# @description Lista el contenido de una carpeta
# ##

from os import listdir, path

carpeta = "cadenas"

if (path.exists(carpeta)):
    for fichero in listdir(carpeta):
        print (fichero)
else:
    print ("La carpeta no existe")