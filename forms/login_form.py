from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nama Pengguna', validators=[DataRequired()], render_kw={"placeholder": "Nama Login Pengguna"})
    password = PasswordField('Kata Sandi', validators=[DataRequired()], render_kw={"placeholder": "Kata Sandi"})
    submit = SubmitField('Masuk')