#coding=utf-8
from flask import Flask, make_response, request
app = Flask(__name__)

@app.route('/')
def principal():
    resp = make_response('Cookie Establecida')
    resp.set_cookie('nombre','Línea de Código')
    return resp

@app.route('/saludo')
def saludo():
    nombre = request.cookies.get('nombre')
    return 'Hola ' + nombre

if __name__ == '__main__':
    app.run()