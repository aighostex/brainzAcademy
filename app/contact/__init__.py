from flask import Blueprint

contact_bp = Blueprint('contact', __name__, template_folder='templates', static_folder='static')

from app.contact import views