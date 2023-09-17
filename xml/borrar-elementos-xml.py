# ##
# @file borrar-elementos-xml.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   16/septiembre/2023
# @url  http://lineadecodigo.com/python/pdte/
# @description Borra un elemento dentro de un fichero XML con Python
# ##

import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

# Recorro todos los nombres del elemento root
# Eliminamos aquellos nombres que acaben en "s"
for elemento in root:
    if (elemento.text[-1] == "s"):
        root.remove(elemento)

tree.write("data4.xml",encoding='utf-8',xml_declaration=True)