from datetime import datetime
import random
from flask import Blueprint, render_template, session

from app.models.batalla import Batalla
from app.repositories.pokemon_repo import obtener_pokemons


battle_bp = Blueprint('battle', __name__, template_folder='templates')

current_year = datetime.now().year


@battle_bp.route('/')
def battles():
    pokemon_selected = session.get('pokemon_selected')
    pokemon_list = obtener_pokemons()
    pokemon_enemy_object = random.choice(pokemon_list)
    session["pokemon_enemy_name"] = pokemon_enemy_object.name
    pokemonPlayer = None
    pokemonEnemy = None
    
    for p in pokemon_list:
        if p.name == pokemon_selected:
            pokemonPlayer = p
            
    all_moves_player = pokemonPlayer.moves
    session["pokemon_player_moves"] = random.sample(all_moves_player, 4)
    
    for p in pokemon_list:
        if p.name == pokemon_enemy_object.name:
            pokemonEnemy = p
            
    all_moves_enemy = pokemonEnemy.moves
    session["pokemon_enemy_moves"]=random.sample(all_moves_enemy, 4)
    
    # session["batalla"]=Batalla(1, datos_pokemon_jugador, datos_pokemon_rival, log, vida_jugador, vida_rival, ataques_jugador, ataques_rival)
    return render_template("battles.html", pokemon=pokemonPlayer, music="static/sounds/inicio.mp3", current_year=current_year)
