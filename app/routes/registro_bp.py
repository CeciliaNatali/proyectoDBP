from flask import Blueprint
from app.controllers.registroController import registrar, registrate


registro_bp= Blueprint('registro_bp', __name__)
registro_bp.route("/registrar", methods=["GET", "POST"]) (registrar)
registro_bp.route("/registrate", methods=["GET", "POST"]) (registrate)

 