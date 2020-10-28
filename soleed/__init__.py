from flask import Flask, request
from soleed.helpers.config import Config
from soleed.helpers.keys import googleAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel 
#import googlemaps


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
mail = Mail(app)
moment = Moment(app)
babel = Babel(app)
#gmaps = googlemaps.Client(key=googleAPI)

#import and initialize modules
from soleed.errors import bp as errors_bp
app.register_blueprint(errors_bp)
from soleed.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
from soleed.main import bp as main_bp
app.register_blueprint(main_bp)
from soleed.development import bp as dev_bp
app.register_blueprint(dev_bp, url_prefix='/development')


if not app.debug:
  if app.config['MAIL_SERVER']:
    auth = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
      auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure = None
    if app.config['MAIL_USE_TLS']:
      secure = ()
    mail_handler = SMTPHandler(
      mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
      fromaddr='no-reply@' + app.config['MAIL_SERVER'],
      toaddrs=app.config['ADMINS'], subject='Soleed Failure',
      credentials=auth, secure=secure)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
  if not os.path.exists('logs'):
    os.mkdir('logs')
  file_handler = RotatingFileHandler('logs/soleed.log', maxBytes=10240, 
  backupCount=10)
  file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)

  app.logger.setLevel(logging.INFO)
  app.logger.info('Soleed startup')

@babel.localeselector
def get_locale():
  # return request.accept_languages.best_match(app.config['LANGUAGES'])
  return 'es'



if __name__ == "__main__":
  app.run(debug=True)


#Import routes (at end to ensure there is no circular import)
import soleed.routes, soleed.models
