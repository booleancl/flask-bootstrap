from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

print(__name__)

@app.route('/')
def hello():
    return __name__

@app.route('/name/<name>')
def name(name):
    return f'Hola {name}!'

@app.route('/req')
def req():
    user_agent = request.headers.get('User-Agent')
    return f'Tu navegador es: {user_agent}'

@app.route('/routes')
def routes():
    print(app.url_map)
    return "Revisa la terminal para ver las rutas"
    