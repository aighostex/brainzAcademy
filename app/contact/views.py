from flask import *
from app.contact import contact_bp

@contact_bp.route('/contact')
def get_contact():
    return render_template('contact.html')