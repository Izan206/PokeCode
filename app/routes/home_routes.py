from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.models.exceptions import TrainerNotFound
from app.models.trainer import Trainer
from app.repositories.battle_repo import get_battle_by_id, get_battles_by_trainer
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
                page = 1
                return redirect(url_for("pokemon.pokedex", page=page))
            except TrainerNotFound:
                error = "Incorrect username or password"

    return render_template('index.html', error=error, current_year=current_year)


@home_bp.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    error = None
    name = None
    password1 = None
    password2 = None

    if request.method == "GET":
        return render_template('sign-up.html', current_year=current_year)

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
            session["trainer_name"] = name
            session["trainer_password"] = password2
            # add_trainer(name, password2)
            return redirect(url_for("home.trainer_skin"))


@home_bp.route('/profile-skin', methods=["GET", "POST"])
def trainer_skin():
    name = session.get("trainer_name", None)
    password = session.get("trainer_password", None)
    selected_skin = "trainer3"
    if request.method == "GET":
        selected_skin = request.args.get("skin", None)
        session["selected_skin"] = selected_skin

    if request.method == "POST":
        selected_skin = session.get("selected_skin", "trainer3")
        action = request.form.get("action", None)
        if action == "save_and_sign_up":
            add_trainer(name, password, selected_skin)
            return render_template("index.html", success="Trainer created successfully! You can log in now.", current_year=current_year)
        if action == "go_back":
            return redirect(url_for("home.sign_up"))

    return render_template("skin_selection.html", current_year=current_year, selected_skin=selected_skin)


@home_bp.route('/Profile')
def profile():
    trainer1 = session.get("trainer")["name"]
    battles = get_battles_by_trainer(trainer1)
    return render_template('profile.html', current_year=current_year, battles=battles)

@home_bp.route('/battle-details/<int:battle_id>')
def battle_details(battle_id):
    if "trainer" not in session:
        return redirect(url_for('home.index'))
        
    battle = get_battle_by_id(battle_id)

    return render_template('battle_details.html', battle=battle, current_year=current_year)

@home_bp.route('/log-out')
def log_out():
    session.clear()
    return redirect(url_for('home.index'))


@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404
