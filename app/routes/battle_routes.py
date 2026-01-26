from datetime import datetime
import random
from flask import Blueprint, redirect, render_template, request, session, url_for
from app.models.battle import Battle
from app.decorators import required_login
from app.models.battle_db import Battle_db
from app.models.trainer import Trainer
from app.repositories.battle_repo import create_battle
from app.repositories.trainer_repo import add_exp, add_lose, add_win, get_random_trainer, get_trainer_by_id
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

    pokemon_player_name = session.get('pokemon_selected')
    pokemon_enemy_name_str = session.get("pokemon_enemy_name")
    pokemon_player_moves = session.get("pokemon_player_moves")
    pokemon_enemy_moves = session.get("pokemon_enemy_moves")
    enemy_trainer = get_random_trainer(session.get("trainer")["name"]).name

    if session.get("battle"):
        battle_temp = session.get("battle")
        if battle_temp.get("player_pokemon_data", {}).get("name") != pokemon_player_name:
            session.pop("battle", None)

    if session.get("battle") is None:
        pokemon_player = obtain_pokemon_by_name(pokemon_player_name)
        pokemon_enemy = obtain_pokemon_by_name(pokemon_enemy_name_str)

        battle = Battle(pokemon_player, enemy_trainer, pokemon_enemy, getLife(pokemon_player), getLife(
            pokemon_enemy), pokemon_player_moves, pokemon_enemy_moves)
        session["battle"] = battle.__dict__
    else:
        battle_data = session.get("battle")
        battle = Battle(**battle_data)
        pokemon_player = battle.player_pokemon_data
        pokemon_enemy = battle.enemy_pokemon_data

    return render_template("battles.html", battle=battle, pokemon=pokemon_player, pokemon_enemy=pokemon_enemy, music="static/sounds/inicio.mp3", current_year=current_year)


@battle_bp.route('/attack', methods=['GET', 'POST'])
@required_login
def attack():
    if request.method == "GET":
        if session["battle"]:
            return redirect(url_for("battle.battles"))
        else:
            return redirect(url_for("pokemon.pokedex"))
    elif request.method == "POST":
        if not session.get("battle"):
            return redirect(url_for("battle.battleResult"))

        move_name = request.form.get("move")
        battle_data = session.get("battle")
        battle = Battle(**battle_data)
        player = battle.player_pokemon_data
        enemy = battle.enemy_pokemon_data

        player_move = getMove(player, move_name)
        player_damage, player_log = calculateDamage(player, enemy, player_move)
        battle.enemy_health, enemy_ko = apply_damage(
            battle.enemy_health, player_damage)
        battle.log.append(player_log)

        if enemy_ko:
            battle.log.append(
                f"{enemy['name']} died and {player['name']} wins!")
            session["battle"] = battle.__dict__
            return redirect(url_for("battle.battleResult"))

        enemy_moves_list = session.get("pokemon_enemy_moves")
        enemy_move = random.choice(enemy_moves_list)
        enemy_damage, enemy_log = calculateDamage(enemy, player, enemy_move)
        battle.player_health, player_ko = apply_damage(
            battle.player_health, enemy_damage)
        battle.log.append(enemy_log)

        if player_ko:
            battle.log.append(
                f"{player['name']} died and {enemy['name']} wins!")
            session["battle"] = battle.__dict__
            return redirect(url_for("battle.battleResult"))

        session["battle"] = battle.__dict__
        return redirect(url_for("battle.battles"))


@battle_bp.route('/result')
@required_login
def battleResult():
    if not session.get("battle"):
        return redirect(url_for("pokemon.pokedex"))

    battle_data = session.get("battle")
    battle = Battle(**battle_data)
    winner, loser = get_battle_result(battle)

    trainer_dict = session.get("trainer")
    trainer_id = trainer_dict["id"]
    trainer = get_trainer_by_id(trainer_id)

    i_win = False
    if winner == session.get('pokemon_selected'):
        i_win = True
        add_win(trainer)
        session["trainer"]["wins"] += 1
        add_exp(trainer, 100)
        session["trainer"]["exp"] += 100
    else:
        add_lose(trainer)
        session["trainer"]["loses"] += 1
        add_exp(trainer, 30)
        session["trainer"]["exp"] += 30

    winnerTrainer = None
    loserTrainer = None
    if i_win:
        winnerTrainer = session.get("trainer")["name"]
        loserTrainer = battle.enemy_trainer
    else:
        winnerTrainer = battle.enemy_trainer
        loserTrainer = session.get("trainer")["name"]

    trainer1 = session.get("trainer")["name"]
    trainer2 = battle.enemy_trainer
    pokemon1 = battle.player_pokemon_data
    pokemon2 = battle.enemy_pokemon_data

    battle_db = Battle_db(trainer_1=trainer1, trainer_2=trainer2, pokemon_1=pokemon1["name"],
                          pokemon_2=pokemon2["name"], winner=winnerTrainer, loser=loserTrainer)
    create_battle(battle_db)

    return render_template("battle_result.html", battle=battle, winner=winner, loser=loser, i_win=i_win)


@battle_bp.route("/rematch")
@required_login
def rematch():
    if not session.get("battle"):
        return redirect(url_for("pokemon.pokedex"))

    battle_data = session.get("battle")
    battle = Battle(**battle_data)

    battle.player_health = getLife(battle.player_pokemon_data)
    battle.enemy_health = getLife(battle.enemy_pokemon_data)
    battle.log = []

    session["battle"] = battle.__dict__

    return redirect(url_for("battle.battles"))
