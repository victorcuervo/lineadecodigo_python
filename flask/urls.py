from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('urls.html')

@app.route('/saludo/dia')
def dia():
    return "Buenos Dias!!!"

@app.route('/saludo/tarde')
def tarde():
    return "Buenas Tardes!!!"

@app.route('/saludo/noche')
def noche():
    return "Buenas Noches!!! Que descanses!!!"



if __name__ == '__main__':
    app.run()