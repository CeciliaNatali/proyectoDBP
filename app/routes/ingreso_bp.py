from flask import Blueprint
from app.controllers.ingresoController import ingresa, registrate


ingreso_bp= Blueprint('ingreso_bp', __name__)


ingreso_bp.route("/", methods=["GET", "POST"]) (ingresa)

ingreso_bp.route("/registro", methods=["GET", "POST"]) (registrate)
