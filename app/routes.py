from app import app #importamos nuestra app
import re #para manipular regular expresiones
from flask import render_template, request #las importar para usarlo en nuestra ruta

from app import db #para mandar solicitudes

#los modelos siguientes nos ayudan a manejar los apis
import requests
import json

#importamos los modelosque vamos utilizar en nuetras rutas
from app.models import User

#para manipular fechas
from datetime import datetime

#varias rutas pueden ser defenidas por la misma funcion

@app.route("/")
@app.route('/index', methods=['GET'])
#la funcionedefine el comportamiento del servidor al ser solicitado
 
def index():
    user={'username':'usuario'}

    return render_template("index.html", title='Moodsica app',user=user, elemento1='codigo',elemento2='HTML')



@app.route("/base")
def base():
    return render_template("base.html")

#En esta parte es la parte de login del usuario

@app.route("/registrate/", methods=["GET", "POST"])
def registrate():
     if request.method == "POST":
         username = request.form["username"]
         password = request.form["password"]
         return "login attempt for username " + username
     return render_template("Registrate.html")
