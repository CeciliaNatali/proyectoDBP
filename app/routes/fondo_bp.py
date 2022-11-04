from flask import Blueprint
from app.controllers.FondoController import aplicar, fondo


fondo_bp = Blueprint('fondo_bp', __name__)
fondo_bp.route("/",methods=["GET"])(fondo)
fondo_bp.route("/aplicar", methods=["GET","POST"]) (aplicar)
