from flask import Flask, redirect,url_for
app = Flask(__name__)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'

@app.route('/saludo')
def saludo():
    return redirect(url_for('holamundo'))


if __name__ == '__main__':
    app.run()