from flask import Blueprint

bp = Blueprint('development', __name__, template_folder = 'templates')


from soleed.development import routes