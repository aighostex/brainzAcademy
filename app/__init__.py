from flask import Flask, render_template



def create_app():
    app = Flask(__name__)
    app.secret_key = 'secretKey'
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # registering blueprint
    from app.past_papers import past_papers_bp
    app.register_blueprint(past_papers_bp)
    
    from app.about import about_bp
    app.register_blueprint(about_bp)

    from app.contact import contact_bp
    app.register_blueprint(contact_bp)
    
    return app