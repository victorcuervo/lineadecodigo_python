from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def holamundo():
    #Definimos una lista
    lista = {'A','B','C','D'}
    return render_template('lista.html',lista=lista)

if __name__ == '__main__':
    app.run()