from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import pdf_routes, email_routes, find_routes