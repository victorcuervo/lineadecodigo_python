from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def holamundo():
    resp = make_response('Respuesta de texto')
    resp.headers['Server'] = 'Mi Servidor'
    return resp

if __name__ == '__main__':
    app.run()