from datetime import datetime
from flask import Blueprint, render_template, request, session

from app.models.battle import Battle
from app.repositories.pokemon_repo import obtainPokemons
from app.services.battle_services import getLife, getMove, obtainEnemyPokemon, obtainPokemonPlayer, simulateAttack


battle_bp = Blueprint('battle', __name__, template_folder='templates')

current_year = datetime.now().year


@battle_bp.route('/')
def battles():
    pokemon_selected = session.get('pokemon_selected')
    pokemon_list = obtainPokemons()

    pokemon_player_moves = session.get("pokemon_player_moves")
    pokemon_enemy_moves = session.get("pokemon_enemy_moves")
    pokemon_player = None
    pokemon_enemy = None

    for p in pokemon_list:
        if p.name == pokemon_selected:
            pokemon_player = p

    pokemon_enemy_name = session.get("pokemon_enemy_name")
    for p in pokemon_list:
        if p.name == pokemon_enemy_name:
            pokemon_enemy = p

    battle = Battle(pokemon_player, pokemon_enemy, getLife(pokemon_player), getLife(
        pokemon_enemy), pokemon_player_moves, pokemon_enemy_moves)
    session["battle"] = battle.__dict__

    return render_template("battles.html", pokemon=pokemon_player, pokemon_enemy=pokemon_enemy, music="static/sounds/inicio.mp3", current_year=current_year)


@battle_bp.route('/attack', methods=['POST'])
def attack():
    move_name = request.form.get("move")
    battle_data = session.get("battle")

    # Aquí podrías reconstruir la batalla desde el diccionario
    battle = Battle(**battle_data)  # o manualmente

    # 1️⃣ Simular el ataque del jugador

    simulateAttack(obtainPokemonPlayer(), obtainEnemyPokemon(), getMove()
                   )
    # 2️⃣ Comprobar si el rival sigue vivo
    # 3️⃣ Si sigue, simular su ataque
    # 4️⃣ Registrar todo en batalla.log
    # 5️⃣ Guardar el nuevo estado en la sesión

    session["battle"] = battle.__dict__
    return render_template("battles.html", battle=battle)
