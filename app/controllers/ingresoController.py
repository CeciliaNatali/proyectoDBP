from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import*
import requests
import json
from cryptography.hazmat.primitives import hashes

def ingreso():
    if request.method == "POST":
        usuario    = request.form["usuario"]
        contrasenna = request.form["contrasenna"]
    
        if not usuario or not contrasenna:
            return "Parametros incompletos."

        try:
            usuario1 = Usuario.query.filter(Usuario.nombre == usuario).first()
            if usuario1 == None or contrasenna != usuario1.contrasenna:
                return "Contraseña y/o usuario inválido."

            #password = bytes(password, "utf-8")
            #digest = hashes.Hash(hashes.SHA256())
            #digest.update(password)
            #hashedPassword = str(digest.finalize())
            #return redirect("/profile?username="+username+"&password="+hashedPassword+"&email="+email)
            return redirect("/cuenta?nombre=" + usuario1.nombre)
        except Exception as err:
            print(err)
            return "Error ingresando a la cuenta. Intente nuevamente."
    return render_template("ingreso.html")

def ingresoAsync():
    body = request.get_json()
    print(body)
    usuario = body["usuario"]
    contrasenna = body["contrasenna"]
    try:
        usuario1 = Usuario.query.filter(Usuario.nombre == usuario).first()
        if usuario1 == None or contrasenna != usuario1.contrasenna:
            return json.dumps({"success": False})
        else:
            return json.dumps({"success": True})
    except:
        return json.dumps({"success": False})

