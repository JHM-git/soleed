
import random
from soleed import app

def schoolFundingLists(inf1, inf2, pri, sec, bac, fp):
  público = []
  concertado = []
  privado = []
  if inf1 == 'público':
    público.append('Infantil Primer Ciclo')
  elif inf1 == 'concertado':
    concertado.append('Infantil Primer Ciclo')
  elif inf1 == 'privado':
    privado.append('Infantil Primer Ciclo')
  if inf2 == 'público':
    público.append('Infantil')
  elif inf2 == 'concertado':
    concertado.append('Infantil')
  elif inf2 == 'privado':
    privado.append('Infantil')
  if pri == 'público':
    público.append('Primaria')
  elif pri == 'concertado':
    concertado.append('Primaria')
  elif pri == 'privado':
    privado.append('Primaria')
  if sec == 'público':
    público.append('Secundaria')
  elif sec == 'concertado':
    concertado.append('Secundaria')
  elif sec == 'privado':
    privado.append('Secundaria')
  if bac == 'público':
    público.append('Bachillerato')
  elif bac == 'concertado':
    concertado.append('Bachillerato')
  elif bac == 'privado':
    privado.append('Bachillerato')
  if fp == 'público':
    público.append('Formación Profesional')
  elif fp == 'concertado':
    concertado.append('Formación Profesional')
  elif fp == 'privado':
    privado.append('Formación Profesional')
  return público, concertado, privado

def facilitiesList(st1, st2, st3):
  facilities_list = []
  if st1 is True:
    facilities_list.append('Patio separado para infantil')
  if st2 is True:
    facilities_list.append('Biblioteca')
  if st3 is True:
    facilities_list.append('Huerto propio')
  return facilities_list

  

test = 'working!'

def opinionSelector(indexlist, list):
  opinion_list = []
  for index in indexlist:
    opinion_list.append(list[index])
  return opinion_list

def oneRandomOpinion(list, indexlist):
  opinion_list = opinionSelector(indexlist, list)
  opinion = random.choice(opinion_list)
  return opinion

def twoRandomOpinions(list, indexlist, score='general_score'):
  opinion_list = opinionSelector(indexlist, list)
  opinion_one = random.choice(opinion_list)
  opinion_list.remove(opinion_one)
  opinion_two = random.choice(opinion_list)
  if opinion_one[score] > opinion_two[score]:
    first_opinion = opinion_one
    second_opinion = opinion_two
  else:
    first_opinion = opinion_two
    second_opinion = opinion_one
  return first_opinion, second_opinion

def strToLs(str):
  #str in form '[item_1 item_2]' - no commas between, '_' instead of whitespace
  ls = str.strip('][').split(' ')
  converted_list = []
  for item in ls:
    new_item = _ToWhitespace(item)
    converted_list.append(new_item)
  return converted_list

def _ToWhitespace(word):
  ls = []
  for char in word:
    new_char = char
    if char == '_':
      new_char = ' '
    ls.append(new_char)
  new_word = ''.join(ls)
  return new_word

#t = moment('2020-09-25T08:47:02Z')




