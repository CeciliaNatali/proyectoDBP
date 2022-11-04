from flask import Blueprint
from app.controllers.CuentaController import cuenta, fondo, playlist, salir, eliminar


cuenta_bp= Blueprint('cuenta_bp', __name__)

cuenta_bp.route("/", methods=["GET"]) (cuenta)
cuenta_bp.route("/buscador", methods=["GET"]) (playlist)
cuenta_bp.route("/playList", methods=["GET"]) (playlist)
cuenta_bp.route("/fondo", methods=["GET", "POST"]) (fondo)
cuenta_bp.route("/salir", methods=["GET"]) (salir)
cuenta_bp.route("/eliminar", methods=["GET","DELETE"]) (eliminar)
