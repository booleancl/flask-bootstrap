from flask import render_template
from app.auth import bp
from app.models.user import User

@bp.route('/login')
def login():
    return render_template('auth/login.html')