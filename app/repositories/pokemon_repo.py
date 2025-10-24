#ACCEDER AL JSON
import json
from pathlib import Path
from flask import render_template
from models.pokemon import Pokemon

#id, name, height, weight, stats, sprints, moves, types
with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    _POKEMONS = json.load(f)
    
def obtener_pokemons():
    pokemons=[]
    for p in _POKEMONS:
        pokemon=Pokemon(**p)
        pokemons.append(pokemon)
    return pokemons

def buscar_por_id(id):
    pokemons=obtener_pokemons()
    pokemon_a_buscar=None
    for pokemon in pokemons:
        if id==pokemon.id:
            pokemon_a_buscar=pokemon
            break
    return pokemon_a_buscar