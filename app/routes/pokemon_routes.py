from datetime import datetime
from flask import Blueprint, current_app, redirect, render_template, request, url_for
from app.forms.trainer_form import trainerForm
from app.services import pokemon_services


pokemon_bp=Blueprint('pokemon', __name__, template_folder='templates')

current_year = datetime.now().year

@pokemon_bp.route('/trainer', methods=["POST"])
def trainer():
    form = trainerForm()
    
    if form.validate_on_submit():
        trainer = request.form.get("trainer")

    if (len(trainer) < 3 or len(trainer) > 15):
        return render_template("index.html", error="The username must have a minimum of 3 characters and a maximum of 15.")
    else:
        return redirect(url_for("pokedex", trainer=trainer))


@pokemon_bp.route('/')  # Pokemons list
def pokedex():
    trainer = request.args.get('trainer')
    pokemon_list = current_app.config["DATA"]
    mensaje_error = request.args.get("mensaje_error")
    return render_template('pokedex.html',  pokemon_list=pokemon_list, music="static/sounds/inicio.mp3", current_year=current_year, trainer=trainer, mensaje_error=mensaje_error)


@pokemon_bp.route("/<int:pokemon_id>")
def pokemon_details(pokemon_id):
    trainer = request.args.get('trainer')
    pokemon=pokemon_services.obtener_pokemon_por_id(pokemon_id)
    if pokemon is None:
        return redirect(url_for("error404"))
    else:
        return render_template("pokemon_details.html", music=url_for('static', filename='sounds/inicio.mp3'), pokemon=pokemon, trainer=trainer, current_year=current_year)
    
@pokemon_bp.route('/pokemon_selected', methods=["POST"])
def pokemon_selected():
    trainer = request.args.get('trainer')
    pokemon_selected = request.form.get('search')
    pokemon_list = current_app.config["DATA"]

    for p in pokemon_list:
        if p['name'] == pokemon_selected.lower():
            return redirect(url_for('battles', pokemon_selected=pokemon_selected.lower()))
    
    mensaje_error = "Pokémon not found, please enter the name correctly"
    return redirect(url_for("pokedex", trainer=trainer, mensaje_error = mensaje_error))