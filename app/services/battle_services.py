import random
from flask import session
from app.services.pokemon_services import list_pokemons


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



def calculateDamage(attacker, defender, move):
    m_name = move["name"]
    m_power = move["power"]
    m_accuracy = move["accuracy"]

    if m_power is None or m_accuracy is None:
        return 0, f"{attacker.name} used {m_name} but it had no effect."

    # fallo según accuracy
    if random.randint(1, 100) > m_accuracy:
        return 0, f"{attacker.name} used {m_name}, but it missed!"

    # Obtener vida del enemigo
    defender_hp = getLife(defender)

    # Daño en proporción a la vida del adversario
    base_damage = (m_power / 100) * defender_hp / 4

    # Factor aleatorio para que el daño varíe un poco
    random_factor = random.uniform(0.85, 1.15)

    damage = int(max(5, base_damage * random_factor))

    log_message = f"{attacker.name} used {m_name}. It hit {damage} of damage!"
    return damage, log_message
