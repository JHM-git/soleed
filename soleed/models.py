
from flask import current_app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time
import jwt
from soleed import db, login

@login.user_loader
def load_user(id):
  return User.query.get(int(id))




class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  headteacher = db.Column(db.Boolean, default=False)
  admin = db.Column(db.Boolean, default=False)
  school_code_number = db.Column(db.String(32), index=True)
  about_me = db.Column(db.String(120))
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)
  opinions = db.relationship('Opinion', backref='author', lazy='dynamic')

  def __repr__(self):
    return '<Usuario {}>'.format(self.username)
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=retro&s={}'.format(digest, size)
  
  def get_reset_password_token(self, expires_in=600):
    return jwt.encode(
      {'reset_password': self.id, 'exp': time() + expires_in},
      current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

  @staticmethod
  def verify_reset_password_token(token):
    try:
      id = jwt.decode(token, current_app.config['SECRET_KEY'],
      algorithm=['HS256'])['reset_password']
    except:
      return
    return User.query.get(id)




class School(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  #info
  name = db.Column(db.String(64), index=True, unique=True)
  telephone = db.Column(db.Integer, index=True, unique=True)
  webpage = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(64), index=True, unique=True)
  code_number = db.Column(db.Integer, index=True, unique=True)
  number_pupils = db.Column(db.Integer, index=True)
  religious = db.Column(db.Boolean, index=True)
  religion = db.Column(db.Integer, db.ForeignKey('religion.id'))
  #location
  address = db.Column(db.String(64), index=True)
  street_number = db.Column(db.String(32), index=True)
  city = db.Column(db.String(32), index=True)
  region = db.Column(db.String(32), index=True)
  subregion = db.Column(db.String(32), index=True)
  borough = db.Column(db.String(32), index=True)
  zone = db.Column(db.String(32), index=True)
  postcode = db.Column(db.Integer, index=True)
  country = db.Column(db.String(32), index=True)
  lat = db.Column(db.String, index=True)
  lng = db.Column(db.String, index=True)
  location_description = db.Column(db.String(500), index=True)
  #director
  headteacher = db.Column(db.String(64), index=True)
  headteacher_title = db.Column(db.String(32), index=True)
  headteacher_email = db.Column(db.String(64), index=True, unique=True)
  headteacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  director_message = db.Column(db.String(1000), index=True)
  #opinions
  opinions = db.relationship('Opinion', backref='school', lazy='dynamic')
  #educational offer
  infantil_primer_ciclo = db.Column(db.Boolean, index=True)
  infantil = db.Column(db.Boolean, index=True)
  primaria = db.Column(db.Boolean, index=True)
  secundaria = db.Column(db.Boolean, index=True)
  bachillerato = db.Column(db.Boolean, index=True)
  formación_profesional = db.Column(db.Boolean, index=True)
  description_infantil_primer_ciclo = db.Column(db.String(1000), index=True)
  description_infantil = db.Column(db.String(1000), index=True)
  description_primaria = db.Column(db.String(1000), index=True)
  description_secundaria = db.Column(db.String(1000), index=True)
  description_bachillerato = db.Column(db.String(1000), index=True)
  description_formación_profesional = db.Column(db.String(1000), index=True)
  #funding
  infantil_primer_ciclo_type = db.Column(db.String(32), index=True)
  infantil_type = db.Column(db.String(32), index=True)
  primaria_type = db.Column(db.String(32), index=True)
  secundaria_type = db.Column(db.String(32), index=True)
  bachillerato_type = db.Column(db.String(32), index=True)
  formación_profesional_type = db.Column(db.String(32), index=True)
  #languages
  trilingual = db.Column(db.Boolean, index=True)
  bilingual = db.Column(db.Boolean, index=True)
  languages = db.relationship('Language', backref='school', lazy='dynamic')
  #facilities
  patio_separado_infantil = db.Column(db.Boolean, index=True)
  library = db.Column(db.Boolean, index=True)
  vegetable_garden = db.Column(db.Boolean, index=True)
  facilities_information = db.Column(db.String(1000), index=True)
  
  #services
  canteen = db.Column(db.Boolean, index=True)
  in_house_kitchen = db.Column(db.Boolean, index=True)
  canteen_price = db.Column(db.Integer, index=True)
  horario_ampliado = db.Column(db.Boolean, index=True)
  horario_ampliado_morning = db.Column(db.String(32), index=True)
  horario_ampliado_afternoon = db.Column(db.String(32), index=True)
  horario_ampliado_price = db.Column(db.Integer, index=True)
  extracurricular_activities = db.Column(db.Boolean, index=True)
  extracurricular_activities_list = db.Column(db.String(500), index=True)
  extracurricular_activities_price_from = db.Column(db.Integer, index=True)
  extracurricular_activities_price_upto = db.Column(db.Integer, index=True)
  nurse = db.Column(db.Boolean, index=True)
  nurse_price = db.Column(db.Integer, index=True)
  school_bus = db.Column(db.Boolean, index=True)
  school_bus_price = db.Column(db.Integer, index=True)
  #bulletpoint_info
  bulletpoint_presentation = db.Column(db.String(500), index=True)
  bulletpoint_methods_and_priorities = db.Column(db.String(500), index=True)
  bulletpoint_specialities = db.Column(db.String(500), index=True)
  #test

  def __repr__(self):
    return '<{}>'.format(self.name)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)


class Language(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  is_obligatory = db.Column(db.Boolean, index=True)
  starting_age = db.Column(db.Integer, index=True)
  weekly_hours = db.Column(db.Integer, index=True)
  description = db.Column(db.String(500), index=True)
  school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
  language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))

  def __repr__(self):
    return '<{}, school: {}>'.format(self.language_id, self.school_id)

class Languages(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  language = db.Column(db.String(32), index=True)

  def __repr__(self):
    return f'{self.language}'



class Religion(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  religion = db.Column(db.String(64), index=True)

  def __repr__(self):
    return f'{self.religion}'

class SportsFacilities(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sports_facility = db.Column(db.String(64), index=True)

  def __init__(self, sports_fac):
    self.sports_facility = sports_fac

  def __repr__(self):
    return f'{self.sports_facility}'

'''
school_languages = db.Table('school_languages',
  db.Column('language_id', db.Integer, db.ForeignKey('religion.id'))
  db.Column('school_id', db.Inteher, db.ForeignKey('school.id'))
)
'''

class Opinion(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  score_general = db.Column(db.Integer, index=True)
  score_teachers = db.Column(db.Integer, index=True)
  score_faculties_materials = db.Column(db.Integer, index=True)
  score_communication_accessibility = db.Column(db.Integer, index=True)
  opinion_general = db.Column(db.String(1000), index=True)
  opinion_teachers = db.Column(db.String(1000), index=True)
  opinion_faculties_materials = db.Column(db.String(1000), index=True)
  opinion_communication_accessibility = db.Column(db.String(1000), index=True)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

  def __repr__(self):
    return '<Opinión: {}'.format(self.opinion_general)



