from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from routes.qa import qa_bp
    from routes.upload import upload_bp

    # Register Blueprints
    app.register_blueprint(upload_bp, url_prefix="/upload")
    app.register_blueprint(qa_bp, url_prefix="/qa")

    return app
