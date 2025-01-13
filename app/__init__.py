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
    

    
    return app