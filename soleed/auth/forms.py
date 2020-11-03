from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from soleed.models import User
from flask_babel import lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Usuario'))
    email = StringField('Correo electronico')
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField(_l('Usuario'), validators=[DataRequired()])
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
            raise ValidationError('Por favor, utliza un correo electronico distinto')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired()])
    submit = SubmitField('Resetea la contraseña')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField('Repite la contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reconfigurar contraseña')
