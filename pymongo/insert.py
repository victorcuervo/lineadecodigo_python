#encoding=utf-8

from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient()

# Seleccionamos la base de datos
db = client.test

# Seleccionamos la colección
users = db.users

# Definimos el documento
user = {
    'nombre': 'Víctor',
    'edad': 38,
    'localidad': 'Avila'
}

# Insertamos el documento
resultado = users.insert_one(user)

print 'Objeto instertado ' + str(resultado.inserted_id)