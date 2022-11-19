from flask import Blueprint
from app.controllers.IndiceController import inicio, acerca,ingresa,registrate


indice_bp = Blueprint('indice_bp', __name__)

indice_bp.route("/", methods=["GET"])(inicio)
indice_bp.route("/acerca", methods=["GET"])(acerca) 
indice_bp.route("/ingreso", methods=["GET"]) (ingresa)
indice_bp.route("/registrate", methods=["GET", "POST"]) (registrate)
