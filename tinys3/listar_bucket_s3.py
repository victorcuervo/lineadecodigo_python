import tinys3

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,'la-prueba',endpoint='s3-eu-west-1.amazonaws.com')

print '-- Inicio del listado --'
lista = conn.list('')

for fichero in lista:
    print fichero['key']

print '-- Fin del Listado --'