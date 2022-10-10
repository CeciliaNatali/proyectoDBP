
from flask import Blueprint
from app.controllers.acercaDeController import Empieza_Ya


acercaDe_bp = Blueprint('acercaDe_bp', __name__)

acercaDe_bp.route("/acercaDe", methods=["GET"]) (Empieza_Ya)

