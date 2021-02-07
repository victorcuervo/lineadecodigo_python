#coding=utf-8
import tinys3

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'
BUCKET = '/vcp-prueba'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,'vcp-prueba',endpoint='s3-eu-west-1.amazonaws.com')

print ('-- Borrado Fichero S3 --')

filename = 'fichero.png'
conn.delete(filename,BUCKET)
print ('Borrado el fichero '+filename)

print ('-- Fin Borrado S3 --')