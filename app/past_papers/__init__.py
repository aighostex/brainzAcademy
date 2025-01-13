from flask import Blueprint

past_papers_bp = Blueprint('past_papers', __name__, template_folder='templates', static_folder='static')

from app.past_papers import views