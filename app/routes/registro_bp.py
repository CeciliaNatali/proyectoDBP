from flask import Blueprint
from app.controllers.RegistroController import registro, registroAsync


registro_bp = Blueprint('registro_bp', __name__)

registro_bp.route("/", methods=["GET", "POST"]) (registro)
registro_bp.route("/async", methods=["POST"]) (registroAsync)
