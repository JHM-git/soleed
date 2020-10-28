from flask import render_template
from soleed.errors import bp
import werkzeug
from werkzeug.exceptions import NotFound, InternalServerError

@bp.app_errorhandler(werkzeug.exceptions.NotFound)
def not_found_error(error):
  return render_template('404.html'), 404

@bp.app_errorhandler(werkzeug.exceptions.InternalServerError)
def internal_error(error):
  db.session.rollback()
  return render_template('500.html'), 500

