from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    description = TextAreaField(label='Deskripsi Soal', validators=[DataRequired()])
    difficulty = StringField(label='Tingkat Kesulitan', validators=[DataRequired()])
    discrimination = StringField('Indeks Daya Beda', validators=[DataRequired()])
    pseudoguess = StringField('Indeks Tebakan Semu', validators=[DataRequired()])

    choice_1 = TextAreaField('Pilihan Jawaban 1', validators=[DataRequired()])
    choice_1_correct = BooleanField('Jawaban Benar')
    choice_2 = TextAreaField('Pilihan Jawaban 2', validators=[DataRequired()])
    choice_2_correct = BooleanField('Jawaban Benar')
    choice_3 = TextAreaField('Pilihan Jawaban 3', validators=[DataRequired()])
    choice_3_correct = BooleanField('Jawaban Benar')
    choice_4 = TextAreaField('Pilihan Jawaban 4', validators=[DataRequired()])
    choice_4_correct = BooleanField('Jawaban Benar')
    choice_5 = TextAreaField('Pilihan Jawaban 5', validators=[DataRequired()])
    choice_5_correct = BooleanField('Jawaban Benar')

    submit = SubmitField('Simpan')
