# ##
# @file crear-carpeta.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   28/enero/2024
# @url  http://lineadecodigo.com/python/crear-una-carpeta-en-python/
# @description Crea una carpera
# ##

from os import mkdir,path

carpeta = 'temp'

if (path.exists(carpeta)):
    print(f"La carpeta {carpeta} ya existe")
else:
    mkdir(carpeta)
    print(f"Carpeta {carpeta} creada")