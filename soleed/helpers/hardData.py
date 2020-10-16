

schoolx = { 
  'id': 1,
  'info': {
    'name': 'Colegio Hipopótamo',
    'location': {
      'address': 'Calle Puente la Reina, 27',
      'city': 'Madrid',
      'postcode': '28050',
      'lat': '40.501473',
      'lng': '-3.677398',
      'description': 'Más información sobre donde se encuentra el colegio, cómo es la zona, qué hay cerca. Si es facil de llegar en transporte público y/o aparcar cerca etc.'
    },
    'telephone': '912 555 555',
    'webpage': 'www.colegiohipopotamo.es',
    'e_mail': 'ejemplo@colegiohipopotamo.es',
    'code_number': '10001000',
    'stages': {
      'Infantil Primer Ciclo': True,
      'Infantil': True,
      'Primaria': True,
      'Secundaria': False,
      'Bachillerato': False,
      'Formación Profesional': False
    },
    'funding': {
      'Infantil Primer Ciclo': 'privado',
      'Infantil Segundo Ciclo (3 años)': 'público',
      'Primaria': 'público',
      'Secundaria': None,
      'Bachillerato': None,
      'Formación Profesional': None
    },
    'numberPupils': '652',
    'languages': {
      'trilingual': 'inglés, francés',
      'bilingual': 'Inglés'
    },
    'beliefs': 'Laico'
  },
  'director': {
    'name': 'Victor Victorius',
    'gender': 'hombre',
    'msg': 'En el Colegio Hipopótamo trabajamos incansablemente para mejorar el futuro de nuestros alumnos. Incorporamos lo más novedoso que el mundo de la educación nos ofrece para siempre estar en vanguardia en la teoría educativa. Los padres forman una parte importante del colegio y estamos continuamente en contacto con ellos, escuchando sus propuestas e intentando solucionar sus problemas.'
  },
  'bulletpoint_info': {
    'presentation': 'Colegio Hipopótamo es un colegio público situado en Las Tablas, en el norte de Madrid. Ofrecemos educación infantil y primaria con posibilidad de cursarlo en bilingüe.',
    'methods_priorities': 'El alumno es el centro de la educación. Nos adaptamos a cada alumno y hacemos un seguimiento exhaustivo sobre las cualidades de cada uno de los niños y niñas que forman nuestro alumnado. Los profesores preparan las clases con las necesidades de sus alumnos en la mente. Hasta tercero de primaria no se hace exámenes, y la evaluación se basa más en la actuación y actividades en clase.',
    'specialities': 'Somos un centro que se adapta a las necesidades de los hijos y en la manera que es posible, a las de los padres. Preparamos los alumnos tanto para la vida real como la académica, y estamos orgullosos de decir que muchos antiguos alumnos han triunfado en sus vidas.'
  },
  'educational_offer': {
    'Infantil Primer Ciclo': 'Descripción de la etapa educativa en unas cinco líneas. Qué quieren destacar, sean métodos, cultura de aprendizaje etcétera. Diferente para cada etapa.',
    'Infantil Segundo Ciclo (3 años)': 'Descripción de la étapa educativa en unas cinco lineas. Qué quieren destacar, sean métodos, cultura de aprendizaje etcetera. Diferente para cada etapa.',
    'Primaria': 'Descripción de la étapa educativa en unas cinco lineas. Qué quieren destacar, sean métodos, cultura de aprendizaje etcetera. Diferente para cada etapa.',
    'Secundaria': False,
    'Bachillerato': False,
    'Formación Profesional': False
  },
  'facilities': {
    'Patio separado para infantil': False,
    'Biblioteca': True,
    'Huerto propio': True,
    'Instalaciones_deportivas': ['Campo de Fútbol', 'Gimnasio', 'Piscina'],
    'information': 'Información general sobre las instalaciones. Cuándo ha sido construido/reformado etc. Qué tipo de espacios hay y cómo se usan. Cómo son las clases y otros espacios interiores.'
  },
  'languages': [
    {
      'language': 'Inglés',
      'optionality': 'obligatorio',
      'description': 'Descripción de la enseñanza del idioma. Si se trata de un sistema bilingüe o no, cuántas horas se dan a la semana, en qué se centra la enseñanza, etc. desde qué edad se empieza a impartir el idioma. El porqué de ese idioma.'
    },
    {
      'language': 'Francés',
      'optionality': 'opcional',
      'description': 'Descripción de la enseñanza del idioma. Si se trata de un sistema bilingüe o no, cuántas horas se dan a la semana, en qué se centra la enseñanza, etc. desde qué edad se empieza a impartir el idioma. El porqué de ese idioma.'
    },
    {
      'language': 'Mandarin',
      'optionality': 'opcional',
      'description': 'Descripción de la enseñanza del idioma. Si se trata de un sistema bilingüe o no, cuántas horas se dan a la semana, en qué se centra la enseñanza, etc. desde qué edad se empieza a impartir el idioma. El porqué de ese idioma.'
    }
  ],
  'services': {
    'comedor': {
      'comedor': True,
      'cocina_propia': False,
      'price': 130
    },
    'horario': {
      'horario_ampliado': True,
      'mañana': '8:00',
      'tarde': '18:30',
      'price': 5.50
    },
    'extraescolares': {
      'provided': True,
      'include': ['Baloncesto', 'Robótica', 'Natación', 'Ajedrez'],
      'price': 35
    },
    'nurse': {
      'available': False,
      'price': None
    },
    'school_bus': {
      'available': True,
      'price': 25
    }
  }
}

opinionsx = {
  'school_id': '1',
  'total_score': 8.5,
  'general_score': 9,
  'teachers_score': 7,
  'faculties_materials_score': 6.5,
  'communication_accessibility_score': 8,
  'number_opinions': 62,
  'index_finders': {
    'general': [0, 1, 2, 3, 4],
    'teachers': [1, 2],
    'faculties_materials': [2],
    'communication_accessibility': [3]
  },
  'opinions': [
    {
    'author': {'username': 'Pablo'},
    'general_score': 9,
    'teachers_score': 8,
    'faculties_materials_score': 8.5,
    'communication_accessibility_score': 7,
    'general': 'Es un colegio muy bueno. Tenemos nuestros dos hijos aquí y estamos contentos la verdad con todo. Una buena elección en el norte de Madrid.',
    'teachers': '',
    'faculties_materials': '',
    'communication_accessibility': ''
    },
    {
    'author': {'username': 'Nuria'},
    'general_score': 5,
    'teachers_score': 7,
    'faculties_materials_score': 6.5,
    'communication_accessibility_score': 6,
    'general': 'No Es un colegio muy bueno. Tenemos nuestros dos hijos aquí y no estamos contentos la verdad con todo. No es una buena elección en el norte de Madrid.',
    'teachers': 'El profesorado lo intenta todo y se nota que ponen todo su empeño en enseñar a sus alumnos, pero por desgracia la dirección del colegio parece querer obstaculizar la tarea de los profesores lo máximo posible, y en cuanto llegamos al último trimestre se ven muchos profesores con la mirada perdida. Cada curos entran nuevos profesores pero siempre ocurre lo mismo.',
    'faculties_materials': '',
    'communication_accessibility': ''  
    },
    {
    'author': {'username': 'Ricardo'},
    'general_score': 8,
    'teachers_score': 10,
    'faculties_materials_score': 9,
    'communication_accessibility_score': 8,
    'general': 'Opinion3',
    'teachers': 'Lalalala lalalalal lalala lalal lal a la l al al al lallala l al lalalala la alla al ala lalal l ala alalala ala la.',
    'faculties_materials': 'El colegio es muy nuevo y el personal lo trata con respeto. Todos los materiales de nuestros hijos, salvo alguna puntual, han sido de muy buena calidad.',
    'communication_accessibility': ''
    },
    {
    'author': {'username': 'Paula'},
    'general_score': 7,
    'teachers_score': 7.5,
    'faculties_materials_score': 9,
    'communication_accessibility_score': 8,
    'general': 'Opinion4.',
    'teachers': '',
    'faculties_materials': '',
    'communication_accessibility': 'Mandan correos electronicos cada semana, y muchas veces con la misma información. A diferencia de muchos colegios, aquí comunican hasta demasiado. Pero no me quejo, siempre sé lo que está ocurriendo en la clase de mi hija.'
    },
    {
    'author': {'username': 'Encarna'},
    'general_score': 6,
    'teachers_score': 6,
    'faculties_materials_score': 6,
    'communication_accessibility_score': 6,
    'general': 'Opinion5.',
    'teachers': '',
    'faculties_materials': '',
    'communication_accessibility': ''
    }
  ]
}

picturesx = {
  'school_id': '1',
  'banner': None,
  'presentation': None,
  'facilities': None
}
