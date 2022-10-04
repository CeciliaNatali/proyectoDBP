from sqlalchemy import Column
from app import db
import email
from datetime import datetime
from encodings import search_function
from msilib.schema import InstallUISequence
from pickle import FALSE

class Usuario(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre      = db.Column(db.String(10), index=True, unique=True)
    email       = db.Column(db.String(70), index=True, unique=True)
    contrasenna = db.Column(db.String(50))
    playlist    = db.relationship('Playlist', backref='usuario', lazy=True, uselist=False)

    def __repr__(self):
        return '<usuario {}>'.format(self.nombre)


class Playlist(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(200))
    usuario_id  = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    canciones   = db.relationship('Cancion', backref='playlist', lazy=True)
    fondo       = db.relationship('Fondo', backref='playlist', lazy=True, uselist=False)

    def __repr__(self):
        return '<playlist_id {}>'.format(self.id)   


class Mood(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag         = db.Column(db.String(20))
    #emoji = db.Column(db.) #imagen
    canciones   = db.relationship('Cancion', backref='mood', lazy=True)

    def __repr__(self):
        return '<mood {}>'.format(self.tag)

class Cancion(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo      = db.Column(db.String(100))
    artista     = db.Column(db.String(50))
    genero      = db.Column(db.String(30))
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    mood_id     = db.Column(db.Integer, db.ForeignKey('mood.id'), nullable=False)

    def __repr__(self):
        return '<cancion {}>'.format(self.titulo)


class Fondo(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre      = db.Column(db.String(20))
    #imagen = db.Column() #imagen
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))

    def __repr__(self):
        return '<fondo {}>'.format(self.nombre)
