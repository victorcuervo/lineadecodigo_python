#coding=utf-8
from flask import Flask
import logging

# Si queremos fichero
#LOG_FILENAME = '/tmp/errores.log'
#logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

# Para la consola
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def principal():
    app.logger.debug('Arranque de la aplicacion')
    app.logger.error('URL no disponible')
    return 'Ejemplo para logs'

if __name__ == '__main__':
    app.run()