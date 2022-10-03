from sqlalchemy import ForeignKey
from app import db
import email
from datetime import datetime
from encodings import search_function
from msilib.schema import InstallUISequence
from pickle import FALSE

#La funcion User nos ayudara para el login del usuario y luego posteriormente
#pasarlo a nuestra base de datos

class Usuario(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario     = db.Column(db.String(10), index=True, unique=True)
    email       = db.Column(db.String(70), index=True, unique=True)
    contrasenna = db.Column(db.String(50))

    #permite imprimir el objeto usuario y mostrar datos
    def __repr__(self):
        return '<user {}>'.format(self.usuario, self.email)

class Playlist(db.Model):
    id    = db.Column(db.Integer, primary_key=True, autoincrement=True, ForeignKey=Usuario) #?
    #agregar foreign key a Usuario
    cancion = db.Column(db.String(100), index=True)
    




