from flask import Flask, render_template, url_for, request, flash, redirect, g
from soleed import db
from soleed.auth import bp
from soleed.models import User
from flask_login import current_user, login_user, logout_user
from soleed.auth.email import send_password_reset_email
from flask_babel import _, get_locale
from soleed.auth.forms import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm

@bp.before_request
def before_request():
  g.locale = str(get_locale())


@bp.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, 
    headteacher=form.headteacher.data, school_code_number=form.school_code_number.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash(_('¡Enhorabuena %(username)s, ya formas parte de nuestra comunidad!', username=user.username))
    return redirect(url_for('auth.login'))
  return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data is not '':
      user = User.query.filter_by(username=form.username.data).first()
    elif form.email.data is not '':
      user = User.query.filter_by(email=form.email.data).first()
    else:
      flash(_('Usuario o Correo electronico requerido para login'))
      return redirect(url_for('auth.login'))
    if user is None or not user.check_password(form.password.data):
      flash(_('Usuario o contraseña no valido'))
      return redirect(url_for('auth.login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('main.index')
    return redirect(url_for('main.index'))
  return render_template('login.html', form=form)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = ResetPasswordRequestForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      send_password_reset_email(user)
    #flash whether user or not makes it impossible to find out whether 
    #an email is member or not - ref MG
    flash(_('Comprueba tu correo electrónico para las instrucciones de cómo resetear tu contraseña'))
    return redirect(url_for('auth.login'))
  return render_template('reset_password_request.html', form=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  user = User.verify_reset_password_token(token)
  if not user:
    return redirect(url_for('main.index'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    user.set_password(form.password.data)
    db.session.commit()
    flash(_('Tu contraseña ha sido reconfigurado.'))
    return redirect(url_for('auth.login'))
  return render_template('reset_password.html', form=form)