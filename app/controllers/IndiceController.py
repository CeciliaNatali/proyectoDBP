from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import User
import requests
import json
from cryptography.hazmat.primitives import hashes

def inicio():
    return render_template("inicio.html")

def acerca():
    return render_template("acercade.html")