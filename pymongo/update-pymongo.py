#encoding=utf-8
from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient()

# Seleccionamos la base de datos
db = client.test

# Seleccionamos la colección
users = db.users


# Documento a buscar para actualizar
searchuser = {
    'nombre': 'Pilar',
    'edad': 30
}

# Insertamos el documento
resultado = users.update_many(searchuser,{"$set": {"edad":31}})

print ('Numero de documentos modificados ' + str(resultado.modified_count))