from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user
from app.auth import bp
from app.models.user import User
from app.extensions import db

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form.get('remember_me')

        if not password:
            flash('La contraseña es obligatoria')
        elif not email:
            flash('El correo es obligatorio')
        else:
            user = User.query.filter_by(email=email).first()
            if user and user.verify_password(password):
                login_user(user, remember)
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('main.index')
                flash(f'Bienvenido { user.username }')
                return redirect(next)
            flash('Usuario o password incorrecto.')
    return render_template('auth/login.html')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        if not username:
            flash('El nombre del usuario es obligatorio')
        elif not email:
            flash('El email es obligatorio') 
        elif not password == password_confirm:
            flash('La contraseña no coincide')     
        else:
            user= User(username = username, email = email, password = password)    
            db.session.add(user)
            db.session.commit()
            flash('Usuario creado correctamente')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')   

@bp.route('logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect('main/index')