#coding=utf-8
import tinys3

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'
BUCKET_ORIGEN = '/bucket-origen'
BUCKET_DESTINO = '/bucket-destino'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,BUCKET_ORIGEN,endpoint='s3-eu-west-1.amazonaws.com')

print '-- Copiar Fichero S3 --'

# Copia entre dos buckets
conn.copy('origen.jpg',BUCKET_ORIGEN,'destino.jpg',BUCKET_DESTINO)

# Copia en el mismo bucket
conn.copy('ORIGEN.jpg',BUCKET_ORIGEN,'destino.jpg')

print '-- Fin Copiar Fichero S3 --'