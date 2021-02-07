#coding=utf-8
import tinys3
from hurry.filesize import size

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'
BUCKET = '/vcp-prueba'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,'vcp-prueba',endpoint='s3-eu-west-1.amazonaws.com')

print ('-- Inicio Metainformación S3 --')
lista = conn.list('')

for fichero in lista:
    print (fichero)
    print ('Clave: ' + fichero['key'])
    print ('Tipo de Almacenamiento: ' + fichero['storage_class'])
    print ('Fecha Modificación: ' + str(fichero['last_modified']))
    print ('ETag: ' + fichero['etag'])
    print ('Tamaño: ' + size(fichero['size']) + ' bytes')
    print ('Tamaño: ' + str(fichero['size']) + ' bytes')


print ('-- Fin Metainformación S3 --')