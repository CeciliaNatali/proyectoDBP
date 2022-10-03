from app import db
import email
from datetime import datetime
from encodings import search_function
from msilib.schema import InstallUISequence
from pickle import FALSE

#La funcion User nos ayudara para el login del usuario y luego posteriormente
#pasarlo a nuestra base de datos

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    #permite imprimir el objeto usuario y mostrar datos
    def __repr__(self):
        return '<user {}>'.format(self.username, self.email)

