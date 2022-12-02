from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user
from app.auth import bp
from app.models.user import User

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user is not None and user.verify_password(request.form['password']):
            login_user(user, request.form['remember_me'])
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Usuario o password incorrecto.')
    return render_template('auth/login.html')

@bp.route('logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect('main.index')