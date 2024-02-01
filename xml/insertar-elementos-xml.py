# ##
# @file insertar-elementos-xml.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   16/septiembre/2023
# @url  http://lineadecodigo.com/python/actualizar-un-fichero-xml-con-python/
# @description Leer un fichero XML con Python
# ##

import xml.etree.ElementTree as ET

tree = ET.parse("xml/data.xml")
root = tree.getroot()

lista_nombres = ['Victor','Ignacio','Elena']

for nombre in lista_nombres:
    nombreElemento = ET.Element("nombre")
    nombreElemento.text = nombre
    root.insert(-1,nombreElemento)


tree.write("data3.xml",encoding='utf-8',xml_declaration=True)