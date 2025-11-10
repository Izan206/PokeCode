from datetime import datetime
import random
from flask import Blueprint, current_app, render_template, request

from app.repositories.pokemon_repo import obtener_pokemons


battle_bp = Blueprint('battle', __name__, template_folder='templates')

current_year = datetime.now().year


@battle_bp.route('/')
def battles():
    pokemon_selected = request.args.get('pokemon_selected')
    pokemon_list = obtener_pokemons()
    pokemon = None
    for p in pokemon_list:
        if p.name == pokemon_selected:
            pokemon = p
    # get 4 randoms moves
    all_moves = pokemon.moves
    moves = random.sample(all_moves, 4)

    # get a random pokemon to fight
    random_pokemon = random.choice(pokemon_list)

    return render_template("battles.html", pokemon=pokemon, moves=moves, random_pokemon=random_pokemon, music="static/sounds/inicio.mp3", current_year=current_year)
