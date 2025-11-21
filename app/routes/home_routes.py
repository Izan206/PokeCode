from datetime import datetime
from flask import Blueprint, redirect, render_template, request, session, url_for

home_bp = Blueprint('home', __name__, template_folder='templates')

current_year = datetime.now().year


@home_bp.route('/', methods=["GET", "POST"])
def index():
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


@home_bp.route('/404')
def error404():
    return render_template('404.html'), 404
