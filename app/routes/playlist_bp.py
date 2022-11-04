from flask import Blueprint
from app.controllers.PlaylistController import agregar, borrar
from app.models import Playlist


playlist_bp= Blueprint('playlist_bp', __name__)

playlist_bp.route("/agregar", methods=["POST"]) (agregar)
playlist_bp.route("/borrar", methods=["GET","DELETE"]) (borrar)
