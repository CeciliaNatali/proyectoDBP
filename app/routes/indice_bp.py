
from flask import Blueprint
from app.controllers.IndiceController import inicio, acerca


inicio_bp = Blueprint('indice_bp', __name__)

inicio_bp.route("/", methods=["GET"]) (inicio)
inicio_bp.route("/acerca", methods=["GET"]) (acerca) 
#inicio_bp.route("/ingreso", methods=["GET"]) (ingresa)
#inicio_bp.route("/registrate", methods=["GET", "POST"]) (registrate)
