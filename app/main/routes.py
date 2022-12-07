from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.app_errorhandler(404)
def page_not_found(error):
        # print(error)
        return render_template('page_not_found.html'), 404