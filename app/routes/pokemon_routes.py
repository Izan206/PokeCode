from datetime import datetime
import random
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.models.trainer import Trainer
from app.repositories.trainer_repo import get_random_trainer, get_trainer_by_id
from app.services import pokemon_services
from app.decorators import required_login


pokemon_bp = Blueprint('pokemon', __name__, template_folder='templates')

current_year = datetime.now().year


@pokemon_bp.route('')
@required_login
def pokedex():
    session.pop("battle", None)
    session.pop("pokemon_selected", None)
    session.pop("pokemon_enemy_name", None)
    session.pop("pokemon_player_moves", None)
    session.pop("pokemon_enemy_moves", None)

    page = request.args.get('page', 1, type=int)
    session["page"] = page

    if (page > 169):
        return redirect(url_for("home.error404"))
    elif (page < 1):
        return redirect(url_for("home.error404"))

    pokemon_list = pokemon_services.list_pokemons(page)
    error_message = session.get("error_message", None)
    return render_template('pokedex.html',  pokemon_list=pokemon_list, music=url_for('static', filename='sounds/inicio.mp3'), current_year=current_year, error_message=error_message, page=page)


@pokemon_bp.route("/<int:pokemon_id>")
@required_login
def pokemon_details(pokemon_id):
    pokemon = pokemon_services.obtain_pokemon_by_id(pokemon_id)
    page = session.get("page")
    if pokemon is None:
        return redirect(url_for("home.error404"))
    else:
        return render_template("pokemon_details.html", page=page, music=url_for('static', filename='sounds/inicio.mp3'), pokemon=pokemon, current_year=current_year)


@pokemon_bp.route('/pokemon_selected', methods=["POST"])
@required_login
def pokemon_selected():
    pokemon_name_input = request.form.get('search').lower()
    page = session.get("page")

    session["pokemon_selected"] = pokemon_name_input
    pokemonEncontrado = pokemon_services.obtain_pokemon_by_name(
        session["pokemon_selected"])

    if pokemonEncontrado:
        all_moves_player = pokemonEncontrado["moves"]
        if len(all_moves_player) < 4:
            session["pokemon_player_moves"] = all_moves_player
        else:
            session["pokemon_player_moves"] = random.sample(
                all_moves_player, 4)

        random_enemy_id = random.randint(1, 151)
        pokemon_enemy_object = pokemon_services.obtain_pokemon_by_id(
            random_enemy_id)

        session["pokemon_enemy_name"] = pokemon_enemy_object["name"]
        all_moves_enemy = pokemon_enemy_object["moves"]

        if len(all_moves_enemy) < 4:
            session["pokemon_enemy_moves"] = all_moves_enemy
        else:
            session["pokemon_enemy_moves"] = random.sample(all_moves_enemy, 4)

        return redirect(url_for('battle.battles'))
    else:
        session["error_message"] = "Pokemon not found enter the name correctly"
        return redirect(url_for("pokemon.pokedex", page=page))
