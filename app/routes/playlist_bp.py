from flask import Blueprint
from app.controllers.playlistController import agregar, borrar,fondo
from app.models import Playlist


playlist_bp= Blueprint('playlist_bp', __name__)

playlist_bp.route("/agregar", methods=["POST"]) (agregar)
playlist_bp.route("/borrar", methods=["GET","DELETE"]) (borrar)
playlist_bp.routte("/fondo", methods=["GET"])(fondo)
