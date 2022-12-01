from flask import Flask
from config import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

#inicializamos la aplicacion
app = Flask(__name__)
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

#importamos las rutas y modelos por si queremos usarlos
from app.routes.indice_bp import indice_bp
from app.routes.ingreso_bp import ingreso_bp
from app.routes.registro_bp import registro_bp
from app.routes.cuenta_bp import cuenta_bp
from app.routes.playlist_bp import playlist_bp
from app.routes.fondo_bp import fondo_bp
from app import models, topRoutes

app.register_blueprint(indice_bp, url_prefix='/indice')
app.register_blueprint(ingreso_bp, url_prefix='/ingreso')
app.register_blueprint(registro_bp, url_prefix='/registro')
app.register_blueprint(cuenta_bp, url_prefix='/cuenta')
app.register_blueprint(playlist_bp, url_prefix='/playlist')
app.register_blueprint(fondo_bp, url_prefix='/fondo')

db.create_all()
