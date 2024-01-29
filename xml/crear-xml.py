# ##
# @file crear-xml.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   17/septiembre/2023
# @url  http://lineadecodigo.com/python/crear-un-fichero-xml-con-python/
# @description Código que crea un fichero XML en Python
# ##

import xml.etree.ElementTree as ET

lista_nombres = ['Victor','Ignacio','Elena']

eNombres = ET.Element("nombres")
for nombre in lista_nombres:
    eNombre = ET.SubElement(eNombres,"nombre")
    eNombre.text = nombre

# Creamos el root
tree = ET.ElementTree(eNombres)

tree.write("new_data.xml",encoding='utf-8',xml_declaration=True)