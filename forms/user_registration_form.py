from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserRegistrationForm(FlaskForm):
    name = StringField('Nama Lengkap', validators=[DataRequired()])
    username = StringField('Nama Login', validators=[DataRequired()])
    password = StringField('Kata Sandi', validators=[DataRequired()])
    submit = SubmitField('Simpan')
