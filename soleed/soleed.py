from soleed import create_app, db 
from soleed.models import User, School, Opinion, Religion, Language, Languages


app = create_app()
app.app_context().push()
#@app.cli.command()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'School': School, 'Opinion': Opinion,
    'Language': Language, 'Languages': Languages, 'Religion': Religion}

if __name__ == "__main__":
  app.run(debug=True)

#Import routes (at end to ensure there is no circular import)


