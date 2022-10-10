
from flask import Blueprint
from app.controllers.fondoController import inicio,ingresa, registrate,acercaDe


inicio_bp = Blueprint('incio_bp', __name__)

inicio_bp.route("/", methods=["GET"]) (inicio)
inicio_bp.route("/ingreso", methods=["GET"]) (ingresa)
inicio_bp.route("/registrate", methods=["GET", "POST"]) (registrate)
inicio_bp.route("/acercaDe", methods=["GET"]) (acercaDe) 