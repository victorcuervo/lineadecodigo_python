#encoding=utf-8

from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient()

# Seleccionamos la base de datos
db = client.usuarios

# Seleccionamos la colección
users = db.users

# Imprimimos el primer resultado
print users.find_one()

