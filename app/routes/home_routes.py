from datetime import datetime
from functools import wraps
from flask import Blueprint, redirect, render_template, request, session, url_for

home_bp = Blueprint('home', __name__, template_folder='templates')

current_year = datetime.now().year


@home_bp.route('/', methods=["GET"])  # Welcome
def index():
    if session.get("invalid_trainer") is None:
        session.pop("invalid_trainer", None)
    return render_template('index.html', music="static/sounds/inicio.mp3", current_year=current_year)


@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404


@home_bp.route('/trainer', methods=["POST"])
def trainer():
    session.pop("invalid_trainer", None)
    session["trainer"] = request.form['trainer']

    if (len(session["trainer"]) < 3 or len(session["trainer"]) > 15):
        session["invalid_trainer"] = "The username must have a minimum of 3 characters and a maximum of 15."
        return redirect(url_for("home.index"))
    else:

        return redirect(url_for("pokemon.pokedex"))
