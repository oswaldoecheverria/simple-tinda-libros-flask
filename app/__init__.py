from flask import Flask, redirect, url_for
from flask import render_template, request
from flask_mysqldb import MySQL

from .models.ModeloLibro import ModeloLibro

app = Flask(__name__)
db = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["usuario"] == "admin"
            and request.form["password"] == "abc123...."
        ):
            return redirect(url_for("index"))
        else:
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route("/libros")
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {"libros": libros}
        return render_template("listado_libros.html", data=data)
    except Exception as ex:
        print(ex)
        return render_template("errores/error.html")


# Manejador error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("errores/404.html"), 404
