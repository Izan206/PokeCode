import random
from flask import session
from app.services.pokemon_services import list_pokemons

# Funciones de logica de la batalla entre pokemons


def obtainPokemonPlayer():
    pokemon_selected = session.get('pokemon_selected')
    for pokemon in list_pokemons():
        if pokemon_selected == pokemon.name:
            return pokemon


def obtainEnemyPokemon():
    pokemon_enemy = session.get('pokemon_enemy')
    for pokemon in list_pokemons():
        if pokemon_enemy == pokemon.name:
            return pokemon


def getMove(pokemon, move_name):
    for move in pokemon.moves:
        if move["name"] == move_name:
            return move
    return


def getLife(pokemon):
    for stat in pokemon.stats:
        if stat["name"] == "hp":
            return stat["value"]


def getPlayerAttacks(moves):
    moves = session.get('pokemon_player_moves')
    return moves


def getEnemyAttacks(moves):
    moves = session.get('pokemon_enemy_moves')
    return moves


# parametros (Objeto del pokemon atacante | Objeto del pokemon defensor | ataque del pokemon atacante)


def simulateAttack(attacker, defender, move):
    m_name = move["name"]
    m_power = move["power"]
    m_accuracy = move["accuracy"]

    if random.randint(1, 100) <= m_accuracy:
        daño = m_power // 3  # puedes ajustar la fórmula
        defender["hp"] -= daño
        defender["hp"] = max(defender["hp"], 0)
        return f"{attacker['name']} uses {m_name}. {defender['name']} lost {daño} PS. PS restantes: {defender['hp']}."
    else:
        return f"{attacker['name']} usó {m_name}. ¡Falló!"
