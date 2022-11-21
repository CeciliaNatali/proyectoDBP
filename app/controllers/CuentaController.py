from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario
import requests
import json
from cryptography.hazmat.primitives import hashes

def eliminar():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasenna = request.form["contrasenna"]

        #Verificando que los parametros esten completos
        if usuario==None or usuario=="" or contrasenna==None or contrasenna=="":
            return "Parametros inválidos."

        viejoUsuario = Usuario.query.filter(Usuario.nombre==usuario).first()

        if viejoUsuario==None or viejoUsuario.contrasenna!=contrasenna:
            return "Usuario y/o contraseña inválido."

        try:
            db.session.delete(viejoUsuario)
            db.session.commit()
        except Exception as err:
            print(err)
            return("Error interno del servidor.")
        
        return redirect("/indice")
    return render_template("eliminarCuenta.html")
    
def buscador():
    pass
def playlist():
    pass
def buscar():
    pass
def fondo():
    pass
def salir():
    pass

def cuenta():
    pass