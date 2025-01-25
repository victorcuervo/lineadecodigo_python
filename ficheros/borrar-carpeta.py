# ##
# @file borrar-carpeta.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/borrar-una-carpeta-en-python/
# @description Borrar una carpeta
# ##

from os import rmdir, path, listdir, remove

carpeta = "temp/borrar"

if (path.exists(carpeta)):
    for fichero in listdir(carpeta):
        fichero = path.join(carpeta,fichero)
        remove(fichero)
        print (f"Borrado el fichero {fichero}")

    rmdir(carpeta)    
    print (f"Borrada la carpeta {carpeta}")

else:
    print ("La carpeta a borrar no existe")


