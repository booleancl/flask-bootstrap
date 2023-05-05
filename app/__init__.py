import os
from flask import Flask
from config import config

from app.extensions import db, migrate, login_manager

environment_config = os.getenv('ENVIRONMENT_CONFIG') or 'default'


def create_app(config_name=environment_config):
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)

    # Register blueprints here:

    # Main blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Messages Blueprint
    from app.messages import bp as messages_bp
    app.register_blueprint(messages_bp, url_prefix='/messages')

    # Authentication Blueprint for Users
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Authentication Blueprint for Admins
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Authentication Blueprint for Teachers
    from app.teacher import bp as teacher_bp
    app.register_blueprint(teacher_bp, url_prefix='/teacher')

    return app
