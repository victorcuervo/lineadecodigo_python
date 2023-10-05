# ##
# @file leer-xml.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   16/septiembre/2023
# @url  http://lineadecodigo.com/python/leer-xml-con-python/
# @description Leer un fichero XML con Python
# ##

import xml.etree.ElementTree as ET

root = ET.parse("data.xml").getroot()

for nombre in root.findall('nombre'):
    print (nombre.text)