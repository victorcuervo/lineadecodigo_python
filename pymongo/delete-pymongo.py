#encoding=utf-8
from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient()

# Seleccionamos la base de datos
db = client.test

# Seleccionamos la colección
users = db.users


# Documento a buscar para actualizar
deleteuser = {
    'nombre': 'Víctor',
    'edad': 50
}

# Insertamos el documento
resultado = users.delete_many(deleteuser)

print 'Numero de documentos eliminados ' + str(resultado.deleted_count)