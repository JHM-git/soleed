from flask import Flask, render_template, url_for, json, request, flash, redirect
from soleed import app, db
from soleed.helpers.hardData import schoolx, opinionsx, picturesx
from soleed.helpers.functions import oneRandomOpinion, twoRandomOpinions, schoolFundingLists
from soleed.helpers.functions import facilitiesList, strToLs
from soleed.helpers.forms import LoginForm, RegistrationForm, EditUserProfileForm, RegisterSchoolForm
from soleed.helpers.forms import EditSchoolForm, ResetPasswordRequestForm, ResetPasswordForm
from soleed.models import User, School, Opinion
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from soleed.helpers.email import send_password_reset_email
from soleed.helpers.keys import googleAPI


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'School': School, 'Opinion': Opinion}

'''
@app.before_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
'''

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/schools')
def schools():
  return render_template('schools.html')

@app.route('/schools/<name>')
def school(name):
  school = School.query.filter_by(name=name).first_or_404()
  #educational offer
  público_list, concertado_list, privado_list = schoolFundingLists(school.infantil_primer_ciclo_type, school.infantil_type, 
  school.primaria_type, school.secundaria_type, school.bachillerato_type, school.formación_profesional_type)
  público = ' '.join(público_list)
  concertado = ' '.join(concertado_list)
  privado = ' '.join(privado_list)
  edu_offer = [school.infantil_primer_ciclo, school.infantil, school.primaria, school.secundaria, 
  school.bachillerato, school.formación_profesional]
  stages = ['Infantil Primer Ciclo', 'Infantil', 'Primaria', 'Secundaria', 'Bachillerato', 'Formación Profesional']
  funding_type = [school.infantil_primer_ciclo_type, school.infantil_type, school.primaria_type, 
  school.secundaria_type, school.bachillerato_type, school.formación_profesional_type]
  edu_stage_msg = [school.description_infantil_primer_ciclo, school.description_infantil, school.description_primaria, 
  school.description_secundaria, school.description_bachillerato, school.description_formación_profesional]
  #facilities
  facilities_list = facilitiesList(school.patio_separado_infantil, school.library, school.vegetable_garden)
  if school.sports_facilities:
    sports_facilities = strToLs(school.sports_facilities)
  else:
    sports_facilities = None
  if school.extracurricular_activities_list:
    extracurricular_activities = strToLs(school.extracurricular_activities_list)  
  else:
    extracurricular_activities = None
  #opinions
  opinions = Opinion.query.filter_by(school_id=school.id).all()
  return render_template('school.html', school=school, público=público, concertado=concertado, 
  privado=privado, pictures=picturesx, opinions=opinions, edu_offer=edu_offer, stages=stages, funding_type=funding_type,
  edu_stage_msg=edu_stage_msg, facilities_list=facilities_list, sports_facilities=sports_facilities, 
  extracurricular_activities=extracurricular_activities, googleAPI=googleAPI)


@app.route('/schools/register school', methods=['GET', 'POST'])
@login_required
def registerSchool():
  if current_user.headteacher is not True:
    flash('Lo sentimos, no puedes acceder a esta página')
    return redirect(url_for('index'))
  form = RegisterSchoolForm()
  if form.validate_on_submit():
    school = School(name=form.name.data, telephone=form.telephone.data, code_number=form.code_number.data, 
    city=form.city.data, headteacher_email=form.headteacher_email.data, headteacher_id=current_user.id)
    db.session.add(school)
    db.session.commit()
    flash('¡' + school.name + ' añadido!')
    return redirect(url_for('school',name=school.name))
  return render_template('register_school.html', form=form)


@app.route('/schools/edit school', methods=['GET', 'POST'])
@login_required
def editSchool():
  if current_user.is_anonymous:
    return redirect(url_for('login'))
  school = School.query.filter_by(headteacher_id=current_user.id).first_or_404()
  form = EditSchoolForm()
  if form.validate_on_submit():
    school.name = form.name.data
    school.telephone = form.telephone.data
    school.webpage = form.webpage.data
    school.email = form.email.data
    school.code_number = form.code_number.data
    school.number_pupils = form.number_pupils.data
    school.address = form.address.data
    school.street_number = form.street_number.data 
    school.city = form.city.data
    school.subregion = form.subregion.data
    school.region = form.region.data
    school.borough = form.borough.data
    school.zone = form.zone.data
    school.postcode = form.postcode.data
    school.country = form.country.data
    school.location_description = form.location_description.data
    if form.religious.data == '1':
      school.religious = True
    elif form.religious.data == '0':
      school.religious = False
    school.religion = form.religion.data
    db.session.add(school)
    db.session.commit()
    flash('Hemos guardado los cambios.')
    return redirect(url_for('school', name=school.name))
  elif request.method == 'GET':
    form.name.data = school.name
    form.telephone.data = school.telephone
    form.webpage.data = school.webpage
    form.email.data = school.email
    form.code_number.data = school.code_number
    form.address.data = school.address
    form.street_number.data = school.street_number
    form.city.data = school.city
    form.subregion.data = school.subregion
    form.region.data = school.region
    form.borough.data = school.borough
    form.zone.data = school.zone
    form.postcode.data = school.postcode
    form.location_description.data = school.location_description
    
  return render_template('edit_school.html', form=form, school=school, googleAPI=googleAPI)



@app.route('/schools/example')
def example_school():
  return render_template('school-example.html', googleAPI=googleAPI)


@app.route('/schools/inProgress')
def schooldev():
  generalOpinionOne, generalOpinionTwo = twoRandomOpinions(opinionsx['opinions'], opinionsx['index_finders']['general'])
  return render_template('school-dev.html', school=schoolx, opinions=opinionsx, 
  pictures=picturesx, generalOpinionOne=generalOpinionOne, generalOpinionTwo=generalOpinionTwo,
  oneRandomOpinion=oneRandomOpinion, googleAPI=googleAPI)


@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  school = School.query.filter_by(headteacher_id=user.id).first()
  opinions = [
    {'author': user, 'body': 'Test opinion #1', 'school_id': 1},
    {'author': user, 'body': 'Test opinion #2', 'school_id': 1}
  ]
  comments = [
    {'author': user, 'body': 'Test comment #1'},
    {'author': user, 'body': 'Test comment #1'}
  ]
  return render_template('user.html', user=user, opinions=opinions, 
  comments=comments, school=school)


@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, 
    headteacher=form.headteacher.data, school_code_number=form.school_code_number.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('¡Enhorabuena ' + user.username + ', ya formas parte de nuestra comunidad!')
    return redirect(url_for('login'))
  return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    if form.username.data is not '':
      user = User.query.filter_by(username=form.username.data).first()
    elif form.email.data is not '':
      user = User.query.filter_by(email=form.email.data).first()
    else:
      flash('Usuario o Correo electronico requerido para login')
      return redirect(url_for('login'))
    if user is None or not user.check_password(form.password.data):
      flash('Usuario o contraseña no valido')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(url_for('index'))
  return render_template('login.html', form=form)


@app.route('/edit_user_profile', methods=['GET', 'POST'])
@login_required
def edit_user_profile():
  form = EditUserProfileForm(current_user.username)
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.about_me = form.about_me.data
    db.session.commit()
    flash('Hemos guardado tus cambios.')
    return redirect(url_for('user', username=current_user.username))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.about_me.data = current_user.about_me
  return render_template('edit_user_profile.html', form=form)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = ResetPasswordRequestForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      send_password_reset_email(user)
    #flash whether user or not makes it impossible to find out whether 
    #an email is member or not - ref MG
    flash('Comprueba tu correo electrónico para las instrucciones de cómo resetear tu contraseña')
    return redirect(url_for('login'))
  return render_template('reset_password_request.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  user = User.verify_reset_password_token(token)
  if not user:
    return redirect(url_for('index'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    user.set_password(form.password.data)
    db.session.commit()
    flash('Tu contraseña ha sido reconfigurado.')
    return redirect(url_for('login'))
  return render_template('reset_password.html', form=form)

@app.route('/logout')
def logout():
  current_user.last_seen = datetime.utcnow()
  db.session.commit()
  logout_user()
  return redirect(url_for('index'))


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')





