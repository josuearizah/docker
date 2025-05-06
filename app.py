from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola a todos! by Josué'

@app.route('/index')
def hola_adso():
    return '¡Hola, como te va?!'

@app.route('/index2')
def hola_adso2():
    return '¡Adso the best!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 