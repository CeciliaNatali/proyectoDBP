from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario
import requests
import json
from cryptography.hazmat.primitives import hashes

def registro():
    if request.method == "POST":
        usuario    = request.form["usuario"]
        email      = request.form["email"]
        contrasenna = request.form["contrasenna"]
        
        #Verificando que los parametros esten completos
        if usuario==None or usuario=="" or email==None or email=="" or contrasenna==None or contrasenna=="":
            return "Parametros inválidos."
        
        # Verificando que el usuario ni email aún no existan
        try:
            usuario1 = Usuario.query.filter(Usuario.nombre == usuario).first()
            usuario2 = Usuario.query.filter(Usuario.email == email).first()
        except Exception as err:
            print(err)
            return("Error interno del servidor.")
        
        if usuario1!=None or usuario2!=None:
            return "Usuario y/o contraseña existentes. Intente denuevo."
        
        # Validando contraseña (POR IMPLEMETAR)
        #if not contraValida(contrasenna):
        #    return "Contraseña inválida."

        nuevoUsuario = Usuario(nombre=usuario, email=email, contrasenna=contrasenna)

        #Ingresando nuevo usuario a la base de datos
        try:
            db.session.add(nuevoUsuario)
            db.session.commit()
        except Exception as err:
            print(err)
            return("Error interno del servidor")
        
        return redirect("/ingreso")
        
    return render_template("registro.html")

def registroAsync():
    body = request.get_json()
    print(body)
    usuario = body["usuario"]
    email = body["email"]
    contrasenna = body["contrasenna"]

    try:
        usuario1 = Usuario.query.filter(Usuario.nombre == usuario).first()
        usuario2 = Usuario.query.filter(Usuario.email == email).first()
    except:
        return json.dumps({"success": False})

    if usuario1!=None or usuario2!=None:
        return json.dumps({"success": False})
    # Validando contraseña (POR IMPLEMETAR)
    #if not contraValida(contrasenna):
    #    return "Contraseña inválida."

    nuevoUsuario = Usuario(nombre=usuario, email=email, contrasenna=contrasenna)

    #Ingresando nuevo usuario a la base de datos
    try:
        db.session.add(nuevoUsuario)
        db.session.commit()
        return json.dumps({"success": True})
    except Exception as err:
        print(err)
        return json.dumps({"success": False})

