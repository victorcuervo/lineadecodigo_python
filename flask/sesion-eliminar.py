#coding=utf-8
from flask import Flask, render_template,request, session


app = Flask(__name__)

@app.route('/')
def principal():
    return 'Ejemplo para eliminar sesion'

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

@app.route('/eliminar-sesion',methods=['GET'])
def eliminar_sesion():
    session.clear()
    return 'La sesión ha sido eliminada'

@app.route('/eliminar-datos-sesion',methods=['GET'])
def eliminar_datos_sesion():
    session.pop('nombre',None)
    return 'Eliminado nombre de la sesion'

app.secret_key = 'esto-es-una-clave-muy-secreta'

if __name__ == '__main__':
    app.run()