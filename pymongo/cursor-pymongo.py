#encoding=utf-8

from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient()

# Seleccionamos la base de datos
db = client.users

# Seleccionamos la colección
listado = db.listado

# Imprimimos el primer resultado
usuarios = listado.find()

for usuario in usuarios:
    print (usuario)

