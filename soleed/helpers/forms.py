from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from soleed.models import User


class LoginForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Correo electronico')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
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


class RegisterSchoolForm(FlaskForm):
    name = StringField('Nombre del colegio', validators=[DataRequired()])
    telephone = StringField('Teléfono', validators=[DataRequired()])
    code_number = StringField('Código del centro', validators=[DataRequired()])
    city = StringField('Ciudad', validators=[DataRequired()])
    headteacher_email = StringField('Correo del director/de la directora', validators=[DataRequired()])
    submit = SubmitField('Registrar colegio')