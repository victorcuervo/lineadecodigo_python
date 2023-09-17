# ##
# @file eliminar-etiquetas-html.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   17/septiembre/2023
# @url  http://lineadecodigo.com/python/pdte/
# @description Elimina las etiquetas HTML de una cadena
# ##

import re

# Reemplazar por expresión regular
codigo_html = "<div><span>Esto es una cadena en <strong>negrita</strong></span></div>"
print (re.sub('<.*?>','',codigo_html))