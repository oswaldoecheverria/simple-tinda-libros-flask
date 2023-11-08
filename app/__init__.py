from flask import Flask, redirect, url_for
from flask import render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
db = MySQL(app)

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

@app.route('/libros')
def listar_libros():
    try:
        cursor=db.connection.cursor()
        sql=""" SELECT l.isbn, l.titulo, l.anioedicion, l.precio, a.apellido, a.nombre
                    FROM libro AS l
                    INNER JOIN autor AS a ON l.autor_id = a.id; """
        cursor.execute(sql)
        #objeto que podemos iterar 
        data=cursor.fetchall()
        data = {
            "libros": data
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        raise Exception(ex)

#Manejador error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404