from app import app #importamos nuestra app
import re #para manipular regular expresiones
from flask import render_template, request
from app import db
import requests
import json
from app.models import Usuario

@app.route("/")
@app.route('/indice', methods=['GET'])
def inicio():
    return render_template("inicio.html")

@app.route("/acercade")
def acerca():
    return render_template("acercade.html")

@app.route("/registro/", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario    = request.form["usuario"]
        email      = request.form["email"]
        contrasena = request.form["contrasenna"]
        return "Intento de registro para el usuario " + usuario
    return render_template("registro.html")

@app.route("/ingreso", methods=["GET", "POST"])
def ingreso():
    if request.method == "POST":
        usuario    = request.form["usuario"]
        contrasena = request.form["contrasenna"]
        return "Intento de ingreso para el usuario " + usuario
    return render_template("ingreso.html")

#completar rutas, metodos y funciones

#@app.route("/micuenta/playlist", methods=[])
#@app.route("/micuenta/playlist/agregar", methods=[])
#@app.route("/micuenta/playlist/borrar", methods=[])
#@app.route("/micuenta/playlist/fondo", methods=[])
#@app.route("/micuenta/playlist/fondo/aplicar", methods=[])

#@app.route("/micuenta/salir", methods=[])
#@app.route("/micuenta/eliminar", methods=[])