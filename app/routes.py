from app import app
import re
from flask import render_template, request
from app import db
import requests
import json

@app.route("/")
def index():
    return render_template("index.html")