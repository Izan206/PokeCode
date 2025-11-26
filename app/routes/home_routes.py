from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for

from app.models.trainer import Trainer
from app.repositories.trainer_repo import add_trainer, get_trainer_by_name

home_bp = Blueprint('home', __name__, template_folder='templates')

current_year = datetime.now().year


@home_bp.route('/', methods=["GET", "POST"])
def index():
    # Falta añadir la logica de validación de usaurio para iniciar sesión
    error = None
    session.clear()
    if request.method == "POST":
        session["trainer"] = request.form.get('trainer', None)

        if session["trainer"] is not None:
            if len(session["trainer"]) < 3 or len(session["trainer"]) > 15:
                error = "The username must have a minimum of 3 characters and a maximum of 15."
                return render_template('index.html', error=error)
            else:
                return redirect(url_for("pokemon.pokedex"))

    return render_template('index.html', error=error)


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
            error = "All fields are required "
            return render_template('sign-up.html', error=error)
        elif len(name) < 3 or len(name) > 15:
            error = "The username must have a minimum of 3 characters and a maximum of 15."
            return render_template('sign-up.html', error=error)
        elif password1 != password2:
            error = "The passwords are not the same"
            return render_template('sign-up.html', error=error)
        elif get_trainer_by_name(name):
            error = "This trainer already exists"
            return render_template('sign-up.html', error=error)

        if error is None:
            trainer = Trainer(name=name, password=password2)
            add_trainer(trainer.name, trainer.password)
            success = "Trainer created successfully"

    return render_template('sign-up.html', success=success)


@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404
