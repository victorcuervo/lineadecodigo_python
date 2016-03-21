#coding=utf-8
from flask import Flask, abort, render_template
app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Ejemplo para páginas de error!'

@app.route('/bloqueado')
def bloqueado():
    return abort(401)

@app.errorhandler(401)
def access_error(error):
    return render_template('error_401.html'), 401

if __name__ == '__main__':
    app.run()
