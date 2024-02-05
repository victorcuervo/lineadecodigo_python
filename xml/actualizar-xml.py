# ##
# @file actualizar-xml.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   16/septiembre/2023
# @url  http://lineadecodigo.com/python/actualizar-un-fichero-xml-con-python/
# @description Leer un fichero XML con Python
# ##

import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
root = tree.getroot()

for nombre in root.findall('nombre'):
    print (nombre.text)
    if (nombre.text == "Curro"):
        nombre.text = "Francisco"
        nombre.set("updated","true")

tree.write("data2.xml",encoding='utf-8',xml_declaration=True)