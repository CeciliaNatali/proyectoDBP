from app import app # importamos nuestra app
import re           # para manipular regular expresiones
from flask import render_template, request
from app import db
import requests
import json
from app.models import *

@app.route('/')
@app.route('/indice', methods=['GET'])
def inicio():
    return render_template("indice.html")

# Listar todos los usuarios
@app.route("/usuarios")
def listarUsuarios():
    #podemos pedir la informacion de varias filas de la tabla
    #al mismo tiempo usando 'query.all()', esto devuelve una lista
    usuarios = Usuario.query.all()
    print(usuarios)
    userStrings = ""
    #podemos iterar por el resultado como cualquier lista
    for usuario in usuarios:
        userStrings += usuario.nombre + " " + usuario.contrasenna + " " + usuario.email + "<br>"
    return userStrings


#completar rutas, metodos y funciones

#@app.route('/indice', methods=['GET'])
#@app.route("/acercade", methods=['GET'])
#@app.route("/registro/", methods=["GET", "POST"])
#@app.route("/ingreso", methods=["GET", "POST"])
#@app.route("/cuenta/playlist/agregar", methods=["POST"])
#@app.route("/cuenta/playlist", methods=["GET"])
#@app.route("/cuenta/playlist/borrar", methods=["GET", "DELETE"])
#@app.route("/cuenta/playlist/fondo", methods=["GET"])
#@app.route("/cuenta/playlist/fondo/aplicar", methods=["GET", "POST"])



#funcion para vereficar la contrasena tenga una longitug mayor o igual a 10

def verifyPassword(password):
    return len(password) >= 10


#------------------------------------------------------
@app.route("/cuenta/playlist/agregar", methods=["POST"])
def AgregarMusica():
        #usamos el try para poder recuperarnos de algun errro
    try:
        #esta ruta espera tres parametros
        args = request.args
       

        descripcion=args.get("description")
        usuario_id=args.get("usuario_id")
        canciones=args.get("canciones")
        fondo=args.get("fondo")

        #utilizaremos el apis en esta parte


    
        #creamos nueva cancion para ser agregado 
        newCancion =Playlist(descripcion=descripcion, usuario_id=usuario_id, canciones=canciones)
        #agregamos la cancion a la sesion actual de la db
        db.session.add(newCancion)
        #mandamos los cambios para que persistan en la db
        db.session.commit()
    #en caso ocurra un error podemos recuperarnos sin romper el flujo del programa    
    except Exception as error:
        print("cancion invalido", error)
        return "Invalid user"       
    return f"cancion {Playlist.descripcion} agregado del usuario {Usuario.nombre} "



#mostramos nuestra lista de musicas en nuestra cuenta

@app.route("/cuenta/playlist", methods=["GET"])
def MiPlaylist(nombre):
    micuenta_usuario=Usuario.playlist.query.all()
    ListMusic=""
    for musica in Usuario.playlist:
        ListMusic +="nombre "+ Usuario.playlist
    return ListMusic.json


   