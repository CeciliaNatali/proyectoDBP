from flask import Blueprint
from app.controllers.CuentaController import cuenta, buscador, fondo, playlist, salir, eliminar, actualizar


cuenta_bp= Blueprint('cuenta_bp', __name__)

cuenta_bp.route("/", methods=["GET"]) (cuenta)
cuenta_bp.route("/buscador", methods=["GET"]) (buscador)
cuenta_bp.route("/playlist", methods=["GET"]) (playlist)
cuenta_bp.route("/fondo", methods=["GET", "POST"]) (fondo)
cuenta_bp.route("/salir", methods=["GET"]) (salir)
cuenta_bp.route("/eliminar", methods=["GET", "POST"]) (eliminar)
cuenta_bp.route("/actualizar", methods=["GET", "POST"]) (actualizar)
