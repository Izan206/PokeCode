from datetime import datetime
import random
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.services import pokemon_services
from app.repositories.pokemon_repo import obtainPokemons
from app.services.auth_services import required_login


pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')

current_year = datetime.now().year


@pokemon_bp.route('/')
@required_login
def pokedex():
    session.pop("battle", None)
    session.pop("pokemon_selected", None)
    session.pop("pokemon_enemy_name", None)
    session.pop("pokemon_player_moves", None)
    session.pop("pokemon_enemy_moves", None)

    pokemon_list = obtainPokemons()
    error_message = session.pop("error_message", None)
    return render_template('pokedex.html',  pokemon_list=pokemon_list, music="static/sounds/inicio.mp3", current_year=current_year, error_message=error_message)


@pokemon_bp.route("/<int:pokemon_id>")
@required_login
def pokemon_details(pokemon_id):
    pokemon = pokemon_services.obtain_pokemon_by_id(pokemon_id)
    if pokemon is None:
        return redirect(url_for("home.error404"))
    else:
        return render_template("pokemon_details.html", music=url_for('static', filename='sounds/inicio.mp3'), pokemon=pokemon, current_year=current_year)


@pokemon_bp.route('/pokemon_selected', methods=["POST"])
@required_login
def pokemon_selected():
    session["pokemon_selected"] = request.form.get('search').lower()
    pokemon_list = obtainPokemons()
    pokemonEncontrado = None
    if pokemon_services.obtain_pokemon_by_name(session["pokemon_selected"]) is not None:
        pokemonEncontrado = pokemon_services.obtain_pokemon_by_name(
            session["pokemon_selected"])

    if pokemonEncontrado:
        # Obtener 4 movimientos aleatorios del pokemon seleccionado
        all_moves_player = pokemonEncontrado.moves
        session["pokemon_player_moves"] = random.sample(
            all_moves_player, 4)
        # Pokemon enemigo
        pokemon_enemy_object = random.choice(pokemon_list)
        session["pokemon_enemy_name"] = pokemon_enemy_object.name
        all_moves_enemy = pokemon_enemy_object.moves
        session["pokemon_enemy_moves"] = random.sample(
            all_moves_enemy, 4)
        return redirect(url_for('battle.battles'))
    else:
        session["error_message"] = "Pokémon not found, please enter the name correctly"
        return redirect(url_for("pokemon.pokedex"))
