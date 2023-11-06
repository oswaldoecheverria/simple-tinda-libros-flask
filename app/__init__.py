from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')


#Manejador error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404