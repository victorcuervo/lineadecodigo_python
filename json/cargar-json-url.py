# ##
# @file cargar-json-url.py
# @version 1.0
# @author Víctor Cuervo - http://lineadecodigo.com
# @date   21/noviembre/2021
# @url  http://lineadecodigo.com/python/cargar-json-desde-una-url-con-python/
# @description Cargar contenido de un fichero JSON desde una URL
# ##

import requests
import json

print(requests.get("https://jsonplaceholder.typicode.com/todos/1"))

response = requests.get("https://jsonplaceholder.typicode.com/todos/1").text
objeto = json.loads(response)
print ("Titulo: " + objeto["title"])