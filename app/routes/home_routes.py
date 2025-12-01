from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.models.exceptions import TrainerNotFound
from app.models.trainer import Trainer
from app.repositories.trainer_repo import add_trainer, get_trainer_by_name
from app.services.auth_services import authenticate

home_bp = Blueprint('home', __name__, template_folder='templates')

current_year = datetime.now().year


@home_bp.route('/', methods=["GET", "POST"])
def index():
    error = None
    if request.method == "GET":
        session.clear()
    elif request.method == "POST":
        nameIntroduced = request.form.get("trainer").lower()
        passwordIntroduced = request.form.get("password")

        if nameIntroduced is None or passwordIntroduced is None:
            error = "Name and password required"
        else:
            try:
                trainer = authenticate(nameIntroduced, passwordIntroduced)
                session["trainer"] = trainer.to_dict()
                return redirect(url_for("pokemon.pokedex"))
            except TrainerNotFound:
                error = "Incorrect username or password"

    return render_template('index.html', error=error, current_year=current_year)


@home_bp.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    error = None
    name = None
    password1 = None
    password2 = None
    success = None
    if request.method == "POST":
        name = request.form.get("name").lower()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not name or not password1 or not password2:
            error = "All fields are required"
        elif len(name) < 3 or len(name) > 15:
            error = "The username must have a minimum of 3 characters and a maximum of 15."
        elif len(password1) <= 3 or len(password2) <= 3:
            error = "The password must have a minimum 4 characters"
        elif password1 != password2:
            error = "The passwords are not the same"
        elif get_trainer_by_name(name):
            error = "This trainer already exists"

        if error:
            return render_template('sign-up.html', error=error)
        elif error is None:
            add_trainer(name, password2)
            success = "Trainer created successfully"

    return render_template('trainer.html', success=success, current_year=current_year)


@home_bp.route('/Profile')
def profile():
    return render_template('profile.html', current_year=current_year)


@home_bp.route('/log-out')
def log_out():
    session.clear()
    return redirect(url_for('home.index'))


@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404
