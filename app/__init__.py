from flask import Flask, redirect, url_for
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['password'] == 'abc123....':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


#Manejador error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404