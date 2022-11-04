from flask import Blueprint
from app.controllers.IngresoController import ingreso, registro


ingreso_bp = Blueprint('ingreso_bp', __name__)


ingreso_bp.route("/", methods=["GET", "POST"]) (ingreso)
ingreso_bp.route("/registro", methods=["GET", "POST"]) (registro)
