from flask import Blueprint
from app.controllers.RegistroController import registro


registro_bp = Blueprint('registro_bp', __name__)

registro_bp.route("/", methods=["GET", "POST"]) (registro)
