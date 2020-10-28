from soleed import app
from models import User, School, Opinion, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'School': School, 'Opinion': Opinion}