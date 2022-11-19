from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import*
import requests
import json
from cryptography.hazmat.primitives import hashes




def registrate():
    if request.method == "POST":
        usuario    = request.form["usuario"]
        email      = request.form["email"]
        contrasena = request.form["contrasenna"]
        return "Intento de registro para el usuario " + usuario
    return render_template("registro.html")

def ingreso():
    return render_template("ingreso.html")