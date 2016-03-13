# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def saludo():
    nombre = 'Victor'
    return render_template('hola_footer.html',nombre=nombre)

if __name__ == '__main__':
    app.run()