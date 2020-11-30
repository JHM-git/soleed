from soleed import db
from soleed.models import Religion, Sports_facilities, Languages, Extracurricular

def religions_to_db():
  catholic = Religion(religion='Católica')
  evangelic = Religion(religion='Evangélica')
  islam = Religion(religion='Islámico')
  db.session.add(catholic)
  db.session.add(evangelic)
  db.session.add(islam)
  db.session.commit()

def languages_to_db():
  eng = Languages(language='inglés')
  fren = Languages(language='francés')
  germ = Languages(language='alemán')
  chi = Languages(language='chino')
  jap = Languages(language='japonés')
  ita = Languages(language='italiano')
  por = Languages(language='portugués')
  db.session.add(eng)
  db.session.add(fren)
  db.session.add(germ)
  db.session.add(chi)
  db.session.add(jap)
  db.session.add(ita)
  db.session.add(por)
  db.session.commit()

def sports_facilities_to_db():
  fut = Sports_facilities('Campo de Futból')
  bal = Sports_facilities('Cancha de Baloncesto')
  gim = Sports_facilities('Gimnasio')
  atl = Sports_facilities('Pista de Atletismo')
  bai = Sports_facilities('Estudio de Danza')
  db.session.add(fut)
  db.session.add(bal)
  db.session.add(gim)
  db.session.add(atl)
  db.session.add(bai)
  db.session.commit()

def extracurriculars_to_db():
  extracurriculars = ['fútbol', 'baloncesto', 'balonmano', 'natación', 'atletismo',
  'patinaje', 'multideporte', 'baile moderno', 'ballet', 'guitarra', 'piano', 'inglés', 'francés',
  'chino', 'portugués', 'italiano', 'gimnasia rítmica', 'judo', 'kung fu', 'música']
  for item in extracurriculars:
    extracurricular = Extracurricular(item)
    db.session.add(extracurricular)
  db.session.commit()

