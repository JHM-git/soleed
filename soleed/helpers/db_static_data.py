from soleed import app, db
from soleed.models import Religion, SportsFacilities, Languages

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
  fut = SportsFacilities('Campo de Futból')
  bal = SportsFacilities('Cancha de Baloncesto')
  gim = SportsFacilities('Gimnasio')
  atl = SportsFacilities('Pista de Atletismo')
  bai = SportsFacilities('Estudio de Danza')
  db.session.add(fut)
  db.session.add(bal)
  db.session.add(gim)
  db.session.add(atl)
  db.session.add(bai)
  db.session.commit()