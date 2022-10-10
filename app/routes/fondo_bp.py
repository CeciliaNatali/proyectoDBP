
from crypt import methods
from flask import Blueprint
from app.controllers.fondoController import aplicar, fondo


fondo_bp = Blueprint('fondo_bp', __name__)
fondo_bp.route("/",methods=["GET"])(fondo)
fondo_bp.route("/fondo", methods=["GET","POST"]) (aplicar)
