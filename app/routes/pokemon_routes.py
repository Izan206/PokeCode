from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from app.services import pokemon_services
from app.repositories.pokemon_repo import obtener_pokemons


pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')

current_year = datetime.now().year


@pokemon_bp.route('/')  # Pokemons list
def pokedex():
    trainer = request.args.get('trainer')
    pokemon_list = obtener_pokemons()
    mensaje_error = request.args.get("mensaje_error")
    return render_template('pokedex.html',  pokemon_list=pokemon_list, music="static/sounds/inicio.mp3", current_year=current_year, trainer=trainer, mensaje_error=mensaje_error)


@pokemon_bp.route("/<int:pokemon_id>")
def pokemon_details(pokemon_id):
    trainer = request.args.get('trainer')
    pokemon = pokemon_services.obtener_pokemon_por_id(pokemon_id)
    if pokemon is None:
        return redirect(url_for("home.error404"))
    else:
        return render_template("pokemon_details.html", music=url_for('static', filename='sounds/inicio.mp3'), pokemon=pokemon, trainer=trainer, current_year=current_year)


@pokemon_bp.route('/pokemon_selected', methods=["POST"])
def pokemon_selected():
    trainer = request.args.get('trainer')
    pokemon_selected = request.form.get('search')
    pokemon_list = obtener_pokemons()

    for p in pokemon_list:
        if p.name == pokemon_selected.lower():
            return redirect(url_for('battle.battles', pokemon_selected=pokemon_selected.lower()))

    mensaje_error = "Pokémon not found, please enter the name correctly"
    return redirect(url_for("pokemon.pokedex", trainer=trainer, mensaje_error=mensaje_error))
