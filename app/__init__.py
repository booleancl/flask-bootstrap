import os
from flask import Flask
from config import config

from app.extensions import db, migrate, login_manager

environment_config = os.getenv('ENVIRONMENT_CONFIG') or 'development'

def create_app(config_name = environment_config):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    # Register blueprints here:

    ## Main blueprint 
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    ## Messages Blueprint 
    from app.messages import bp as messages_bp
    app.register_blueprint(messages_bp, url_prefix='/messages')

    ## Authentication Blueprint
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app