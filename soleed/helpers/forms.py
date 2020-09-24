from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms import IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from soleed.models import User, School


class LoginForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Correo electronico')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    headteacher = BooleanField('Soy director/a')
    school_code_number = StringField('Código del centro')
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repite la contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrate')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, elige un usuario distinto')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, utliza un correo elctronico distinto')


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


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired()])
    submit = SubmitField('Resetea la contraseña')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repite la contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reconfigurar contraseña')


class RegisterSchoolForm(FlaskForm):
    name = StringField('Nombre del colegio', validators=[DataRequired()])
    telephone = StringField('Teléfono', validators=[DataRequired()])
    code_number = StringField('Código del centro', validators=[DataRequired()])
    city = StringField('Ciudad', validators=[DataRequired()])
    headteacher_email = StringField('Correo del director/de la directora', validators=[DataRequired()])
    submit = SubmitField('Registrar colegio')

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
    name = name = StringField('Nombre del colegio', validators=[DataRequired()])
    telephone = StringField('Teléfono', validators=[DataRequired()])
    webpage = StringField('Página web', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired()])
    code_number = StringField('Código del centro', validators=[DataRequired()])
    number_pupils = IntegerField('Número de alumnos', validators=[DataRequired()])
    religious = RadioField('Vocación', choices=[(1, 'religioso'), (0, 'laico')], 
    validators=[DataRequired()])
    religion = StringField('Religion')
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

    submit = SubmitField('Registrar los cambios')


