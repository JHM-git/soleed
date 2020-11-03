from flask import render_template, url_for, json, request, flash
from flask import redirect, g, current_app
from soleed import db
from soleed.helpers.hardData import schoolx, opinionsx, picturesx
from soleed.helpers.functions import oneRandomOpinion, twoRandomOpinions, schoolFundingLists
from soleed.helpers.functions import facilitiesList, strToLs, edu_offer_lstMaker, tuple_maker
from soleed.main.forms import EditUserProfileForm, RegisterSchoolForm
from soleed.main.forms import EditSchoolForm, LanguageForm
from soleed.models import User, School, Opinion, Language, Religion, SportsFacilities, Languages
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from soleed.helpers.keys import googleAPI
from flask_babel import _, get_locale
from soleed.main import bp


@bp.before_app_request
def before_request():
  g.locale = str(get_locale())




@bp.route('/')
@bp.route('/index')
def index():
  return render_template('index.html')


@bp.route('/schools')
def schools():
  schools = School.query.all()
  return render_template('schools.html', schools=schools)

@bp.route('/schools/<name>')
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
  #if school.sports_facilities:
  #  sports_facilities = strToLs(school.sports_facilities)
  #else:
  #  sports_facilities = None
  if school.extracurricular_activities_list:
    extracurricular_activities = strToLs(school.extracurricular_activities_list)  
  else:
    extracurricular_activities = None
  #opinions
  opinions = Opinion.query.filter_by(school_id=school.id).all()
  return render_template('school.html', school=school, público=público, concertado=concertado, 
  privado=privado, pictures=picturesx, opinions=opinions, edu_offer=edu_offer, stages=stages, funding_type=funding_type,
  edu_stage_msg=edu_stage_msg, facilities_list=facilities_list, 
  extracurricular_activities=extracurricular_activities, googleAPI=googleAPI)


@bp.route('/schools/register school', methods=['GET', 'POST'])
@login_required
def registerSchool():
  if current_user.headteacher is not True and current_user.admin is not True:
    flash(_('Lo sentimos, no puedes acceder a esta página'))
    return redirect(url_for('main.index'))
  if School.query.filter_by(headteacher_id=current_user.id).first() is not None:
    flash(_('No puedes registrar más de un colegio. Para editar tu colegio, vea tu perfil'))
    return redirect(url_for('main.index'))
  form = RegisterSchoolForm()
  edu_offer = ''
  if form.validate_on_submit():
    school = School(name=form.name.data, telephone=form.telephone.data, code_number=form.code_number.data, 
    email=form.email.data, headteacher=form.headteacher.data, headteacher_email=form.headteacher_email.data, 
    headteacher_id=current_user.id, address=form.address.data, street_number=form.street_number.data, 
    city=form.city.data, subregion=form.subregion.data, region=form.region.data, borough=form.borough.data, 
    zone=form.zone.data, postcode=form.postcode.data, country=form.country.data)
    edu_offer = form.educational_offer.data
    for n in edu_offer:
      if n == '1':
        school.infantil_primer_ciclo = True
      elif n == '2':
        school.infantil = True
      elif n == '3':
        school.primaria = True
      elif n == '4':
        school.secundaria = True
      elif n == '5':
        school.bachillerato = True
      elif n == '6':
        school.formación_profesional == True
    school.infantil_primer_ciclo_type = form.infantil_primer_ciclo_type.data
    school.infantil_type = form.infantil_type.data
    school.primaria_type = form.primaria_type.data
    school.secundaria_type = form.secundaria_type.data
    school.bachillerato_type = form.bachillerato_type.data
    school.formación_profesional_type = form.formación_profesional_type.data
    db.session.add(school)
    db.session.commit()
    flash('¡' + school.name + ' añadido!')
    return redirect(url_for('main.school',name=school.name))
  return render_template('register_school.html', form=form, googleAPI=googleAPI, edu_offer=edu_offer)


@bp.route('/schools/edit school', methods=['GET', 'POST'])
@login_required
def edit_school():
  if current_user.is_anonymous:
    return redirect(url_for('auth.login'))
  school = School.query.filter_by(headteacher_id=current_user.id).first_or_404()
  form = EditSchoolForm()
  language_form = LanguageForm()
  edu_offer_lst = []
  if language_form.validate_on_submit():
    languages_db = Language.query.filter_by(school_id=school.id).all()
    language_ids = []
    languages = []
    for lan in languages_db:
      language_ids.append(lan.language_id)
    for lid in language_ids:
      languages.append(Languages.query.filter_by(id=lid).first())
    if language_form.language.data in languages:
      flash('Idioma ya está en la oferta del colegio. Puedes editarlo abajo')
      return redirect(url_for('main.edit_school'))
    
    language = Languages.query.filter_by(language=language_form.language.data).first()
    language_to_db = Language(language_id=language.id, 
starting_age=language_form.starting_age.data, weekly_hours=language_form.weekly_hours.data, 
description=language_form.description.data, school_id=school.id)
    if language_form.is_obligatory.data == '1':
      language_to_db.is_obligatory = True
    elif language_form.is_obligatory.data == '0':
      language_to_db.is_obligatory = False
    db.session.add(language_to_db)
    db.session.commit()
    flash('idioma añadido')
    return redirect(url_for('main.edit_school'))
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
      school.religion = form.religion.data
    elif form.religious.data == '0':
      school.religious = False
      school.religion = None
    edu_offer = form.educational_offer.data
    for n in edu_offer:
      if n == '1':
        school.infantil_primer_ciclo = True
      elif n == '2':
        school.infantil = True
      elif n == '3':
        school.primaria = True
      elif n == '4':
        school.secundaria = True
      elif n == '5':
        school.bachillerato = True
      elif n == '6':
        school.formación_profesional == True
    school.infantil_primer_ciclo_type = form.infantil_primer_ciclo_type.data
    school.infantil_type = form.infantil_type.data
    school.primaria_type = form.primaria_type.data
    school.secundaria_type = form.secundaria_type.data
    school.bachillerato_type = form.bachillerato_type.data
    school.formación_profesional_type = form.formación_profesional_type.data
    school.description_infantil_primer_ciclo = form.description_infantil_primer_ciclo.data
    school.description_infantil = form.description_infantil.data
    school.description_primaria = form.description_primaria.data
    school.description_secundaria = form.description_secundaria.data
    school.description_bachillerato = form.description_bachillerato.data
    school.description_formación_profesional = form.description_formación_profesional.data
    school.headteacher = form.headteacher.data
    school.headteacher_email = form.headteacher_email.data
    school.headteacher_title = form.headteacher_title.data
    school.director_message = form.director_message.data
    school.bulletpoint_presentation = form.bulletpoint_presentation.data
    school.bulletpoint_methods_and_priorities = form.bulletpoint_methods_and_priorities.data
    school.bulletpoint_specialities = form.bulletpoint_specialities.data
    db.session.add(school)
    db.session.commit()
    flash(_('Hemos guardado los cambios.'))
    return redirect(url_for('main.school', name=school.name))
  elif request.method == 'GET':
    form.name.data = school.name
    form.telephone.data = school.telephone
    form.webpage.data = school.webpage
    form.email.data = school.email
    form.code_number.data = school.code_number
    form.religion.data = school.religion
    form.address.data = school.address
    form.street_number.data = school.street_number
    form.city.data = school.city
    form.subregion.data = school.subregion
    form.region.data = school.region
    form.borough.data = school.borough
    form.zone.data = school.zone
    form.postcode.data = school.postcode
    form.location_description.data = school.location_description
    edu_offer_boolean = [school.infantil_primer_ciclo, school.infantil, school.primaria, 
    school.secundaria, school.bachillerato, school.formación_profesional]
    edu_offer_ids = ['educational_offer-0', 
            'educational_offer-1', 'educational_offer-2', 'educational_offer-3', 
            'educational_offer-4', 'educational_offer-5']
    edu_offer_lst = edu_offer_lstMaker(edu_offer_boolean, edu_offer_ids)
    form.infantil_primer_ciclo_type.data = school.infantil_primer_ciclo_type
    form.infantil_type.data = school.infantil_type
    form.primaria_type.data = school.primaria_type
    form.secundaria_type.data = school.secundaria_type
    form.bachillerato_type.data = school.bachillerato_type
    form.formación_profesional_type.data = school.formación_profesional_type
    form.description_infantil_primer_ciclo.data = school.description_infantil_primer_ciclo
    form.description_infantil.data = school.description_infantil
    form.description_primaria.data = school.description_primaria
    form.description_secundaria.data =school.description_secundaria
    form.description_bachillerato.data = school.description_bachillerato
    form.description_formación_profesional.data = school.description_formación_profesional
    form.headteacher.data = school.headteacher
    form.headteacher_email.data = school.headteacher_email
    form.headteacher_title.data = school.headteacher_title
    form.director_message.data = school.director_message
    form.bulletpoint_presentation.data = school.bulletpoint_presentation
    form.bulletpoint_methods_and_priorities.data = school.bulletpoint_methods_and_priorities
    form.bulletpoint_specialities.data = school.bulletpoint_specialities
  return render_template('edit_school.html', form=form, school=school, language_form=language_form, 
  googleAPI=googleAPI, edu_offer_lst=edu_offer_lst)



@bp.route('/user/<username>')
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








@bp.route('/edit_user_profile', methods=['GET', 'POST'])
@login_required
def edit_user_profile():
  form = EditUserProfileForm(current_user.username)
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.about_me = form.about_me.data
    db.session.commit()
    flash(_('Hemos guardado tus cambios.'))
    return redirect(url_for('main.user', username=current_user.username))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.about_me.data = current_user.about_me
  return render_template('edit_user_profile.html', form=form)



@bp.route('/logout')
def logout():
  current_user.last_seen = datetime.utcnow()
  db.session.commit()
  logout_user()
  return redirect(url_for('main.index'))


@bp.route('/about')
def about():
  return render_template('about.html')


@bp.route('/contact')
def contact():
  return render_template('contact.html')


from soleed.soleed import db






