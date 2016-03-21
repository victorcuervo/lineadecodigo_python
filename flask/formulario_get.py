from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def principal():
    return 'Ejemplo para mensajes'

@app.route('/saludo',methods=['GET'])
def formulario():

    #Comprobamos si viene el parametro por GET
    try:
        nombre = request.args.get('nombre')

        if (nombre != ''):
            return 'Hola ' + nombre
        else:
            return render_template('formulario_get.html')
    except:
        return render_template('formulario_get.html')

if __name__ == '__main__':
    app.run()