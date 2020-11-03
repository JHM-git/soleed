from flask import Flask, request, current_app
from soleed.config import Config
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
from flask_babel import lazy_gettext as _l
#import googlemaps



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Por favor, haz el login para acceder a esta página')
mail = Mail()
moment = Moment()
babel = Babel()
#gmaps = googlemaps.Client(key=googleAPI)

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  with app.app_context():
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

  

    #import and initialize modules
    from soleed.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    from soleed.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from soleed.main import bp as main_bp
    app.register_blueprint(main_bp)
    from soleed.development import bp as dev_bp
    app.register_blueprint(dev_bp, url_prefix='/development')

    if not app.debug and not app.testing:
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

  return app


@babel.localeselector
def get_locale():
  # return request.accept_languages.best_match(current_app.config['LANGUAGES'])
  return 'es'



#if __name__ == "__main__":
#  app.run(debug=True)


#Import routes (at end to ensure there is no circular import)
from soleed import models
