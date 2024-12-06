from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import pdf_routes, email_routes, find_routes, bs_routes, system_monitor_routes
from .network_routes import bp as network_bp

def init_app(app):
    app.register_blueprint(network_bp)

