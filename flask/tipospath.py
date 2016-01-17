from flask import Flask
app = Flask(__name__)

@app.route('/fichero/<path:ruta>',methods=['GET'])
def fichero(ruta):
    return 'Ruta del fichero ' + ruta

if __name__ == '__main__':
    app.run()