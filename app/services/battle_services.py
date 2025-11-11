import random

from flask import session
import app.repositories.pokemon_repo
from app.services.pokemon_services import listar_pokemons

#Funciones de logica de la batalla entre pokemons

def obtenerDatosPokemonJugador():
    pokemon_selected=session.get('pokemon_selected');
    for pokemon in  listar_pokemons():
        if pokemon_selected==pokemon.name:
            return pokemon
    

def obtenerDatosPokemonEnemigo():
    pokemon_enemy=session.get('pokemon_enemy');
    for pokemon in  listar_pokemons():
        if pokemon_enemy==pokemon.name:
            return pokemon
    

def obtenerVida(pokemon):
    for p in listar_pokemons():
        if p.name==pokemon.name:
            for stat in p.stats:
                if stat.name=="hp":
                    return stat.value
                
def obtenerAtaqueJugador(moves):
    moves=session.get('pokemon_player_moves')
    return moves

def obtenerAtaqueEnemigo(moves):
    moves=session.get('pokemon_enemy_moves')
    return moves
    