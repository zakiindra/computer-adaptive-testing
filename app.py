from flask import Flask, render_template, jsonify, flash, redirect, url_for
from flask_login import current_user, login_user, LoginManager, login_required, logout_user

from config import Config
from forms.login_form import LoginForm
from forms.question_form import QuestionForm
from dependencies import question_service, user_service
from forms.user_registration_form import UserRegistrationForm

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)


@login.user_loader
def user_loader(id):
    return user_service.get_user_by_id(id)


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', page='index')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if not user_service.exists_by_name(form.username.data):
            flash('Nama pengguna tidak ditemukan')
        if not user_service.check_password(form.username.data, form.password.data):
            flash('Kata sandi yang dimasukkan salah')
        user = user_service.get_user_by_username(form.username.data)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', login_form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/questions')
@login_required
def questions():
    all_questions = question_service.get_all_questions()
    return render_template('questions.html', page='questions', questions=all_questions)


@app.route('/questions/create', methods=['GET', 'POST'])
@login_required
def add_question():
    question_form = QuestionForm()
    if question_form.validate_on_submit():
        if question_service.create_question(question_form):
            return redirect(url_for('add_question'))
    return render_template('create_question.html', form=question_form, page='questions')


@app.route('/users')
def users():
    all_users = user_service.get_all_member_users()
    return render_template('users.html', page='users', users=all_users)


@app.route('/users/create', methods=['GET', 'POST'])
@login_required
def add_user():
    user_registration_form = UserRegistrationForm()
    if user_registration_form.validate_on_submit():
        if user_service.register_member_user(user_registration_form):
            return redirect(url_for('add_user'))
        else:
            flash('Nama login sudah didaftarkan. Silakan masukkan nama login lain.')
    return render_template('create_user.html', form=user_registration_form, page='users')


@app.route('/results')
def results():
    return render_template('results.html', page='results')

# @app.route('/questions/<id>/edit', methods=['GET', 'POST'])
# def edit_question(id):
#     question =
#


if __name__ == '__main__':
    app.run(debug=True)
