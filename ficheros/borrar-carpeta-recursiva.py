# ##
# @file borrar-carpeta-recursiva.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/borrar-carpetas-de-forma-recursiva-en-python/
# @description Borra una carpeta y todo su contenido de forma recursiva
# ##

from os import rmdir, path, listdir, remove

def borrar_carpeta(carpeta):
    if (path.exists(carpeta)):
        for fichero in listdir(carpeta):
            fichero = path.join(carpeta,fichero)
            if path.isdir(fichero):
                borrar_carpeta(fichero)
            else:
                remove(fichero)
                print (f"Borrado el fichero {fichero}")
        rmdir(carpeta)
        print (f"Borrada la carpeta {carpeta}")
    else:
        print ("La carpeta a borrar no existe") 


carpeta = "temp/borrar"
borrar_carpeta(carpeta)