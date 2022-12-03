from app import app
import re
from flask import render_template, request, redirect, jsonify
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
    body = request.get_json()
    print(body)
    usuario = body["usuario"]
    contrasenna = body["contrasenna"]

    viejoUsuario = Usuario.query.filter(Usuario.nombre==usuario).first()

    if viejoUsuario==None or viejoUsuario.contrasenna!=contrasenna:
        return json.dumps({"success": False})

    try:
        db.session.delete(viejoUsuario)
        db.session.commit()
        return json.dumps({"success": True})
    except Exception as err:
        print(err)
        return json.dumps({"success": False})

def actualizar():
    body = request.get_json()
    usuario = body["usuario"]
    viejaContra = body["viejaContra"]
    nuevaContra = body["nuevaContra"]

    usuario1 = Usuario.query.filter(Usuario.nombre==usuario).first()
    if usuario1 == None or usuario1.contrasenna != viejaContra:
        return json.dumps({"success": False})

    if usuario1 and (usuario1.contrasenna == viejaContra):
        usuario1.contrasenna = nuevaContra
    
    try:
        db.session.commit()
        return json.dumps({"success": True})
    except Exception as err:
        print(err)
        return json.dumps({"success": False})
    
def buscador():
    body = request.get_json()
    tag    = body["tag"]
    yearmin = body["yearmin"]
    yearmax = body["yearmax"]
    #print(body)

    url = "http://musicovery.com/api/V6/playlist.php?&fct=getfromtag&tag="+tag+"&yearmin="+yearmin+"&yearmax="+yearmax
    result = requests.get(url, verify=False).json()
    result = result["tracks"]["track"]
    #print(type(result))
    nuevaLista = []
    for element in result:
        nuevaLista.append({"titulo":element["title"],"artista": element["artist_display_name"], "genero":element["genre"]})
        #print(element.keys())
    #print(nuevaLista)

    #print(json.dumps(result, indent=4))
    return jsonify({"success": True, "result": nuevaLista})




def playlist():
    pass
def fondo():
    pass
def salir():
    pass

