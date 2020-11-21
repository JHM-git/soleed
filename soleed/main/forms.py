from flask import request, current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms import IntegerField, SelectField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, Optional
from soleed.models import User, School, Religion, Languages, Language, Sports_facilities
from soleed.models import Extracurricular
from flask_babel import lazy_gettext as _l
from soleed.helpers.functions import range_list, tuple_maker
from soleed.main import bp
from flask_login import current_user

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class EditUserProfileForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    about_me = TextAreaField('¿Quién soy?', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enviar')

    def __init__(self, original_username, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Por favor, elige un usuario distinto')




class RegisterSchoolForm(FlaskForm):
    #General
    name = StringField('Nombre del colegio', validators=[DataRequired()])
    telephone = StringField('Teléfono', validators=[DataRequired()])
    code_number = StringField('Código del centro', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired()])
    headteacher = StringField('Director/a', validators=[DataRequired()])
    headteacher_email = StringField('Correo del director/de la directora', validators=[DataRequired()])
    #Location
    address_search = StringField('Encuentra tu dirección')
    address = StringField('Nombre de via', validators=[DataRequired()])
    street_number = StringField('Número')
    city = StringField('Ciudad', validators=[DataRequired()])
    subregion = StringField('Provincia', validators=[DataRequired()])
    region = StringField('Comunidad autónoma', validators=[DataRequired()])
    borough = StringField('Barrio')
    zone = StringField('Zona')
    postcode = StringField('Código postal', validators=[DataRequired()])
    country = StringField('Pais')
    lat = StringField('Latitud')
    lng = StringField('Longitud')
    submit = SubmitField('Registrar colegio')
    #educational offer
    educational_offer = MultiCheckboxField('Etapas educativas', choices=[('1', 'Infantil Primer Ciclo'), 
    ('2', 'Infantil Segundo Siglo (3 años)'), ('3', 'Primaria'), ('4', 'Secundaria'), ('5', 'Bachillerato'), 
    ('6', 'Formación Profesional')], validators=[DataRequired()])
    #funding
    infantil_primer_ciclo_type = RadioField('Infantil Primer Ciclo', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')
    infantil_type = RadioField('Infantil (3 años)', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')
    primaria_type = RadioField('Primaria', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')
    secundaria_type = RadioField('Secundaria', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')
    bachillerato_type = RadioField('Bachillerato', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')
    formación_profesional_type = RadioField('Formación Profesional', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')], default='0')

    def validate_code_number(self, code_number):
        school = School.query.filter_by(code_number=code_number.data).first()
        if school is not None:
            raise ValidationError('Código del colegio erroneo')
    
    def validate_headteacher_email(self, headteacher_email):
        school = School.query.filter_by(headteacher_email=headteacher_email.data).first()
        if school is not None:
            raise ValidationError('Elige otro correo electrónico')

class EditSchoolForm(FlaskForm):
    #General
    name = StringField('Nombre del colegio', validators=[DataRequired()])
    telephone = StringField('Teléfono', validators=[DataRequired()])
    webpage = StringField('Página web', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired()])
    code_number = StringField('Código del centro', validators=[DataRequired()])
    number_pupils = IntegerField('Número de alumnos', validators=[DataRequired()])
    religious = RadioField('Vocación', choices=[(1, 'religioso'), (0, 'laico')], 
    validators=[DataRequired()])
    religion_choices = Religion.query.all()
    religion = SelectField('Religion', choices=tuple_maker(religion_choices))
    #Location
    address_search = StringField('Encuentra tu dirección')
    address = StringField('Nombre de via', validators=[DataRequired()])
    street_number = StringField('Número')
    city = StringField('Ciudad', validators=[DataRequired()])
    subregion = StringField('Provincia', validators=[DataRequired()])
    region = StringField('Comunidad autónoma', validators=[DataRequired()])
    borough = StringField('Barrio')
    zone = StringField('Zona')
    postcode = StringField('Código postal', validators=[DataRequired()])
    country = StringField('Pais')
    lat = StringField('Latitud')
    lng = StringField('Longitud')
    location_description = TextAreaField('Descripción de la ubicación del colegio', validators=[Length(min=0, max=500)])
    #educational offer
    educational_offer = MultiCheckboxField('Etapas educativas', choices=[('1', 'Infantil Primer Ciclo'), 
    ('2', 'Infantil Segundo Siglo (3 años)'), ('3', 'Primaria'), ('4', 'Secundaria'), ('5', 'Bachillerato'), 
    ('6', 'Formación Profesional')], validators=[DataRequired()])
    description_infantil_primer_ciclo = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    description_infantil = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    description_primaria = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    description_secundaria = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    description_bachillerato = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    description_formación_profesional = TextAreaField('Descripción:', 
    validators=[Length(min=0, max=750)])
    #funding
    infantil_primer_ciclo_type = RadioField('Infantil Primer Ciclo', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    infantil_type = RadioField('Infantil (3 años)', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    primaria_type = RadioField('Primaria', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    secundaria_type = RadioField('Secundaria', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    bachillerato_type = RadioField('Bachillerato', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    formación_profesional_type = RadioField('Formación Profesional', choices=[('0', 'No aplicable'), ('público', 'Público'), 
    ('concertado', 'Concertado'), ('privado', 'Privado')])
    #headteacher msg & bulletpoints
    headteacher = StringField('Director/a', validators=[DataRequired()])
    headteacher_email = StringField('Correo del director/de la directora', validators=[DataRequired()])
    headteacher_title = SelectField('Título del director/de la directora', choices=[('Sr', 'Sr'), ('Sra', 'Sra'), ('Dr', 'Dr'), ('Dra', 'Dra')])
    director_message = TextAreaField('Mensaje del director/de la directora', validators=[Length(min=0, max=750)])
    bulletpoint_presentation = TextAreaField('Presentación del colegio', validators=[Length(min=0, max=500)])
    bulletpoint_methods_and_priorities = TextAreaField('Los métodos de aprendizaje y las prioridades en la enseñanza', validators=[Length(min=0, max=500)])
    bulletpoint_specialities = TextAreaField('¿En qué se direfencia el colegio de otros?', validators=[Length(min=0, max=500)])
    #languages
    monolingual = BooleanField('No')
    bilingual = BooleanField('Bilingüe')
    trilingual = BooleanField('Trilingüe')
    bi_tri_languages = MultiCheckboxField('Elige el/los idioma/s', choices=[])
    #facilities
    patio_separado_infantil = BooleanField('Patio separado para Infantil')
    library = BooleanField('Biblioteca')
    vegetable_garden = BooleanField('Huerto propio')
    sports_facs = Sports_facilities.query.all()
    sports_facilities_list = []
    for fac in sports_facs:
        sports_facilities_list.append(fac.sports_facility)
    sports_facilities = MultiCheckboxField('Instalaciones deportivas', choices=tuple_maker(sports_facilities_list))
    facilities_information = TextAreaField('Información sobre las instalaciones del colegio', validators=[Length(min=0, max=500)])
    #services
    canteen = BooleanField('Comedor')
    in_house_kitchen = BooleanField('Con cocina propia')
    canteen_price = IntegerField('Precio al mes', validators=[Optional()])
    horario_ampliado = BooleanField('Horario ampliado')
    horario_ampliado_morning = SelectField('mañanas desde', choices=tuple_maker(['7:00', '7:30', '8:00', '8:30']))
    horario_ampliado_afternoon = SelectField('tardes hasta', choices=tuple_maker(['16:00', '16:30', '17:00', '17:30', '18:00', '18:30']))
    horario_ampliado_price = IntegerField('precio por franja al día', validators=[Optional()])
    nurse = BooleanField('Enfermeria')
    nurse_price = IntegerField('Precio al mes', validators=[Optional()])
    school_bus = BooleanField('Transporte')
    school_bus_price = IntegerField('Precio al mes', validators=[Optional()])
    extracurricular_activities_offered = BooleanField('Se ofrece extraescolares')
    extracurricular_activities_price_from = IntegerField('precios desde', validators=[Optional()])
    extracurricular_activities_price_upto = IntegerField('precios hasta al mes', validators=[Optional()])
    extracurriculars = Extracurricular.query.all()
    extracurriculars_list = []
    for activity in extracurriculars:
        extracurriculars_list.append(activity.activity)
    extracurricular_activities = MultiCheckboxField('Extraescolares ofrecidos', choices=tuple_maker(extracurriculars_list))

    
    submit = SubmitField('Registrar los cambios')


class LanguageForm(FlaskForm):
    language_selection = Languages.query.all()
    language = SelectField('El idioma', choices=tuple_maker(language_selection), validators=[DataRequired()])
    is_obligatory = RadioField('¿Es obligatorio?', choices=[(0, 'No'), (1, 'Sí')])
    starting_age = SelectField('Edad de comienzo', choices=range_list(17), validators=[DataRequired()])
    weekly_hours = IntegerField('Horas semanales', validators=[DataRequired()])
    description = TextAreaField('Descripción del idioma y su enseñanza')
    
    submit = SubmitField('Añadir idioma')



class EditLanguageForm(LanguageForm, FlaskForm):
    language = SelectField('El idioma', choices=[], validators=[DataRequired()])
    is_obligatory = None
    edit_is_obligatory = RadioField('¿Es obligatorio?', choices=[(0, 'No'), (1, 'Sí')], validators=[DataRequired()])
    submit = SubmitField('Cambiar los datos del idioma')

class RemoveLanguageForm(FlaskForm):
    language = SelectField('El idioma', choices=[], validators=[DataRequired()])

    submit = SubmitField('Quitar el idioma')



    

