from flask import *
from app.past_papers import past_papers_bp

@past_papers_bp.route('/past_papers_list')
def get_past_papers_list():
    return render_template('list_papers.html')