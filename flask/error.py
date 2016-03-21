#coding=utf-8
from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Ejemplo para páginas de error!'

@app.route('/bloqueado')
def bloqueado():
    return abort(401)

@app.route('/peticion',methods=['POST'])
def peticion():
    return abort(405)

if __name__ == '__main__':
    app.run()
