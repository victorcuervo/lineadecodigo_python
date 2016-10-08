#coding=utf-8
from flask import Flask, render_template,request, session
import os

app = Flask(__name__)

@app.route('/')
def principal():
    return 'Ejemplo manejo de sesion'

@app.route('/saludo',methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/saludo',methods=['POST'])
def saludo():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    session['nombre'] = nombre
    session['apellido'] = apellido
    return 'Hola ' + nombre + ' ' + apellido

@app.route('/datos-sesion',methods=['GET'])
def datos_sesion():
    if 'nombre' in session:
        n = session['nombre']
    else:
        n= ''

    if 'apellido' in session:
        a = session['apellido']
    else:
        a = ''

    return 'Datos Sesion: ' + n + ' ' + a


app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run()