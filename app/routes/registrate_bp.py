from flask import Blueprint
from app.controllers.RegistrateController import ingreso, registrate


registrate_bp = Blueprint('registrate_bp', __name__)


registrate_bp.route("/", methods=["GET", "POST"]) (registrate)
registrate_bp.route("/registro", methods=["GET", "POST"]) (ingreso)
