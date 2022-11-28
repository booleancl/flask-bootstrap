from flask import Flask, render_template
from config import Config

from app.extensions import db
from app.extensions import migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app,db)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.messages import bp as messages_bp
    app.register_blueprint(messages_bp, url_prefix='/messages')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    @app.route('/usuario/<name>')
    def user(name):
        return render_template('user.html', user = name)

    @app.route('/usuario')
    def user_incognito():
        return render_template('user.html')

    @app.route('/navegador')    
    def browser():
        user_agent = request.headers.get('User-Agent')
        return f'Tu navegador es: {user_agent}'

    @app.route('/rutas')    
    def routes():
        print(app.url_map)
        return 'Revisa tu consola para ver las rutas'

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 400

    return app