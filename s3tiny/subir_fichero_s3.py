import tinys3

S3_ACCESS_KEY = 'BAKIBAKI678H67HGA'
S3_SECRET_KEY = '+vpOpILD+E9872AialendX0Ui123CKCKCKw'
BUCKET = 'la-prueba'

conn = tinys3.Connection(S3_ACCESS_KEY,S3_SECRET_KEY,endpoint='s3-eu-west-1.amazonaws.com')

print 'Leyendo fichero'
f = open('../resources/foto.png','rb')

print 'Haciendo upload'
conn.upload('foto2.png',f,BUCKET)

print 'Fichero subido a S3'