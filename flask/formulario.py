from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def principal():
    return 'Ejemplo para mensajes'

@app.route('/saludo',methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/saludo',methods=['POST'])
def saludo():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    return 'Hola ' + nombre + ' ' + apellido

if __name__ == '__main__':
    app.run()