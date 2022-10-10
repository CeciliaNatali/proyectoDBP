from flask import Blueprint
from app.controllers.miCuentaController import cuenta,eleminar, PLaylist, salir


miCuenta_bp= Blueprint('miCuenta_bp', __name__)

miCuenta_bp.route("/", methods=["GET"]) (cuenta)
miCuenta_bp.route("/eleminar", methods=["GET","DELETE"]) (eleminar)
miCuenta_bp.route("/miPlayList", methods=["GET"]) (PLaylist)
miCuenta_bp.routte("/salir", methods=["GET"])(salir)
