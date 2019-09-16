from flask_wtf import FlaskForm
from wtforms import RadioField


class AnswerForm(FlaskForm):
    choices = RadioField(choices=['A', 'B', 'C', 'D', 'E'])
