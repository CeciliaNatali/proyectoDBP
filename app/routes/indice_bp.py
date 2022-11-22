from flask import Blueprint
from app.controllers.IndiceController import inicio, acerca


indice_bp = Blueprint('indice_bp', __name__)

indice_bp.route("/", methods=["GET"])(inicio)
indice_bp.route("/acerca", methods=["GET"])(acerca) 
