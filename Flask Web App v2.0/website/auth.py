#  настройка URL-адресов
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db  # из файла __init__.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

#  http://127.0.0.1:5000/login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        user = User.query.filter_by(email=email).first()
        if user:    # сравнение хешированого пароля с паролем пользователя
            if check_password_hash(user.password, password):
                flash('Успешный вход в систему', category='success')
                login_user(user, remember=True)  # запоминание входа до очищения истории
                return redirect(url_for('views.home'))
            else:
                flash('Пароль неверен, повторите попытку', category='error')
        else:
            flash('e-mail не зарегистрирован в системе', category='error')

    return render_template("login.html", user=current_user)

#  http://127.0.0.1:5000/logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#  http://127.0.0.1:5000/sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email      = request.form.get('email')
        first_name = request.form.get('firstName')
        password1  = request.form.get('password1')
        password2  = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('e-mail уже был зарегистрирован', category='error')
        elif len(email) < 4:
            flash('e-mail слишком короткий (меньше 4 символов)', category='error')
        elif len(first_name) < 2:
            flash('Имя слишком короткое (меньше 2 символов)', category='error')
        elif password1 != password2:
            flash('пароли не совпадают', category='error')
        elif len(password1) < 7:
            flash('Пароль слишком короткий (меньше 7 символов)', category='error')
        else:  # успешное добавление пользователя в базу данных  first_name (models.py) = first_name
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)  # запоминание входа до очищения истории
            flash('Создана учетная запись', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)