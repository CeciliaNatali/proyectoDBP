from flask import Blueprint
from app.controllers.IngresoController import ingreso, ingresoAsync


ingreso_bp = Blueprint('ingreso_bp', __name__)

ingreso_bp.route("/", methods=["GET", "POST"]) (ingreso)
ingreso_bp.route("/async", methods=["POST"]) (ingresoAsync)

