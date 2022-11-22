from app import app
import re
from flask import render_template, request, redirect
from app import db
from app.models import Usuario
import requests
import json
from cryptography.hazmat.primitives import hashes
from app.templates import *

def inicio():
    return render_template("indice.html")

def acerca():
    return render_template("acercaDe.html")