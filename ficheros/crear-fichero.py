# ##
# @file crear-fichero.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  https://lineadecodigo.com/blog/crear-un-fichero-en-python/
# @description Crea un fichero
# ##

with open("fichero.txt","w") as fichero:
    fichero.write("Contenido del fichero\n")
    fichero.write("Más Contenido en el fichero\n")
    fichero.write("Última fila del fichero\n")
    