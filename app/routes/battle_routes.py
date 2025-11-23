from datetime import datetime
import random
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.models.battle import Battle
from app.services.auth_services import required_login
from app.services.battle_services import apply_damage, calculateDamage, getLife, getMove, get_battle_result
from app.services.pokemon_services import obtain_pokemon_by_name


battle_bp = Blueprint('battle', __name__, template_folder='templates')

current_year = datetime.now().year


@battle_bp.route('/')
@required_login
def battles():
    if not session.get("pokemon_selected") or not session.get("pokemon_enemy_name"):
        session.pop("battle", None)
        session.pop("pokemon_selected", None)
        session.pop("pokemon_enemy_name", None)
        session.pop("pokemon_player_moves", None)
        session.pop("pokemon_enemy_moves", None)
        return redirect(url_for("pokemon.pokedex"))

    pokemon_selected = session.get('pokemon_selected')
    pokemon_player_moves = session.get("pokemon_player_moves")
    pokemon_enemy_moves = session.get("pokemon_enemy_moves")
    pokemon_enemy_name = session.get("pokemon_enemy_name")
    pokemon_player = obtain_pokemon_by_name(pokemon_selected)
    pokemon_enemy = obtain_pokemon_by_name(pokemon_enemy_name)

    battle = Battle(pokemon_player, pokemon_enemy, getLife(pokemon_player), getLife(
        pokemon_enemy), pokemon_player_moves, pokemon_enemy_moves)
    session["battle"] = battle.__dict__

    return render_template("battles.html", battle=battle, pokemon=pokemon_player, pokemon_enemy=pokemon_enemy, music="static/sounds/inicio.mp3", current_year=current_year)


@battle_bp.route('/attack', methods=['POST'])
@required_login
def attack():
    if not session.get("battle"):
        return redirect(url_for("battle.battleResult"))

    move_name = request.form.get("move")
    battle_data = session.get("battle")
    battle = Battle(**battle_data)
    player = battle.player_pokemon_data
    enemy = battle.enemy_pokemon_data

    # Turno jugador
    player_move = getMove(player, move_name)
    player_damage, player_log = calculateDamage(player, enemy, player_move)
    battle.enemy_health, enemy_ko = apply_damage(battle.enemy_health, player_damage)
    battle.log.append(player_log)

    if enemy_ko:
        battle.log.append(f"{enemy.name} died and {player.name} wins!")
        session["battle"] = battle.__dict__
        return redirect(url_for("battle.battleResult"))

    # Turno enemigo
    enemy_moves_list = session.get("pokemon_enemy_moves")
    enemy_move = random.choice(enemy_moves_list)
    enemy_damage, enemy_log = calculateDamage(enemy, player, enemy_move)
    battle.player_health, player_ko = apply_damage(battle.player_health, enemy_damage)
    battle.log.append(enemy_log)

    if player_ko:
        battle.log.append(f"{player.name} died and {enemy.name} wins!")
        session["battle"] = battle.__dict__
        return redirect(url_for("battle.battleResult"))

    session["battle"] = battle.__dict__
    return render_template("battles.html", pokemon=player, pokemon_enemy=enemy, battle=battle, music="static/sounds/inicio.mp3", current_year=current_year)


@battle_bp.route('/result')
@required_login
def battleResult():
    if not session.get("battle"):
        return redirect(url_for("pokemon.pokedex"))

    battle_data = session.get("battle")
    battle = Battle(**battle_data)
    winner, loser=get_battle_result(battle)

    return render_template("battle_result.html", battle=battle, winner=winner, loser=loser,)
