from flask import Flask, render_template
app = Flask(__name__,static_folder='static')

@app.route('/')
def holamundo():
    return render_template('hola_estaticos.html')

if __name__ == '__main__':
    app.run()
