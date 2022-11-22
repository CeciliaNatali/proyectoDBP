from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario
import requests
import json
from cryptography.hazmat.primitives import hashes

def cuenta():
    usuario = request.args
    nombre = usuario.get("nombre")
    contrasenna = usuario.get("contrasenna")
    email = usuario.get("email")

    return render_template("cuenta.html", usuario=nombre, contrasenna=contrasenna, email=email)

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

def actualizar():
    if request.method == "POST":
        usuario = request.form["usuario"]
        viejaContra = request.form["viejaContra"]
        nuevaContra = request.form["nuevaContra"]

        #if not viejaContra and not viejoUsuario:
        #    return "Requiere al menos un parámetro a actualizar."

        usuario1 = Usuario.query.filter(Usuario.nombre==usuario).first()
        if usuario1 == None or usuario1.contrasenna != viejaContra:
            return "Usuario inválido y/o contraseña inválidos."
        
        if usuario1 and (usuario1.contrasenna == viejaContra):
            usuario1.contrasenna = nuevaContra
        try:
            db.session.commit()
        except Exception as err:
            print("Error al actualizar ", err)
            return "Error interno del servidor al actualizar, porfavor intente nuevamente."
        return redirect("/cuenta?nombre=" + usuario1.nombre)
    return render_template("actualizar.html")
    
def buscador():
    return render_template("buscador.html")
def playlist():
    pass
def buscar():
    pass
def fondo():
    pass
def salir():
    pass

