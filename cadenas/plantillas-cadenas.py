
# ##
# @file plantillas-cadenas.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   6/octubre/2023
# @url  http://lineadecodigo.com/python/pdte/
# @description Uso de f-string o interpolación de cadenas
# ##

from string import Template

t = Template('Hola, $nombre!')
print (t.substitute(nombre='Victor'))