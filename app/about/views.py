from flask import *
from app.about import about_bp

@about_bp.route('/about')
def get_about():
    return render_template('about.html')