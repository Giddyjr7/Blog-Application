import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Basic config (override with environment variables in production)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Where to redirect non-authenticated users for @login_required
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "warning"

    # Import models so that they are registered with SQLAlchemy
    from . import models  # noqa: F401

    # Register routes blueprint
    from .routes import main as main_bp
    app.register_blueprint(main_bp)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
