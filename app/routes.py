from app import app #importamos nuestra app
import re #para manipular regular expresiones
from flask import render_template, request
from app import db
import requests
import json
from app.models import *

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

#@app.route('/indice', methods=['GET'])
#@app.route("/acercade", methods=['GET'])
#@app.route("/registro/", methods=["GET", "POST"])
#@app.route("/ingreso", methods=["GET", "POST"])
#@app.route("/micuenta/eliminar", methods=["GET", "DELETE"])
#@app.route("/micuenta/playlist/agregar", methods=["POST"])
#@app.route("/micuenta/playlist", methods=["GET"])

#@app.route("/micuenta/playlist/borrar", methods=["GET", "DELETE"])
#@app.route("/micuenta/playlist/fondo", methods=["GET"])
#@app.route("/micuenta/playlist/fondo/aplicar", methods=["GET", "POST"])
#@app.route("/micuenta/salir", methods=["GET"])



#Eliminar cuenta
@app.route("/micuenta/eliminar", methods=["GET", "DELETE"])
def deleteCuenta(nombre):
    usuario = Usuario.query.filter(Usuario.nombre ==nombre).first()

    if usuario == None:
        return "Usuario no encontrado"
    
    db.session.delete(usuario)
    try:
        db.session.commit()
    except Exception as err:
        return "Eliminacion invalida"
    return "Usuario Eliminado"



@app.route("/add/user", methods=['GET'])
def agregarUsuario():
    #usamos el try para poder recuperarnos de algun errro
    try:
        #esta ruta espera tres parametros
        args = request.args
        nombre = args.get("nombre")
        contrasenna = args.get("contrasenna")
        email = args.get("email")
        #el usuario podria no mandar los parametros, hay que verificar que sean validos
        if (nombre == None):
            return "Falta parametro nombre"
        elif (contrasenna == None):
            return "Falta parametro contrasenna"
        elif (email == None):
            return "Falta parametro email"
        
        if (not verifyPassword(contrasenna)):
            return "Contrasena invalida"
        #creamos un nuevo usuario de clase User 
        newUser = Usuario(nombre=nombre, contrasenna=contrasenna, email=email)
        #agregamos el usuario a la sesion actual de la db
        db.session.add(newUser)
        #mandamos los cambios para que persistan en la db
        db.session.commit()
    #en caso ocurra un error podemos recuperarnos sin romper el flujo del programa    
    except Exception as error:
        print("Usuario invalido", error)
        return "Invalid user"       
    return "usuario agregado"



#funcion para vereficar la contrasena tenga una longitug mayor o igual a 10

def verifyPassword(password):
    return len(password) >= 10


#------------------------------------------------------
@app.route("/micuenta/playlist/agregar", methods=["POST"])

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

@app.route("/micuenta/playlist", methods=["GET"])
def MiPlaylist(nombre):
    micuenta_usuario=Usuario.playlist.query.all()
    ListMusic=""
    for musica in Usuario.playlist:
        ListMusic +="nombre "+ Usuario.playlist
    return ListMusic.json


   
