#coding=utf-8
import tinys3

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'
BUCKET = '/vcp-prueba'
DIRECTORIO = '/midirectorio/'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,BUCKET,endpoint='s3-eu-west-1.amazonaws.com')

print ('-- Borrado Directorio S3 --')

lista = conn.list(DIRECTORIO,BUCKET)

# Borramos todos los ficheros del directorio
for fichero in lista:
    conn.delete(fichero['key'])

# Borramos el directorio
conn.delete(DIRECTORIO)

print ('-- Fin Borrado Directorio S3 --')