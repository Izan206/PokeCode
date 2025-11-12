#ACCEDER AL JSON
import json
from pathlib import Path
from app.models.pokemon import Pokemon

#id, name, height, weight, stats, sprints, moves, types
with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    _POKEMONS = json.load(f)
    
def obtainPokemons():
    pokemons=[]
    for p in _POKEMONS:
        pokemon=Pokemon(**p)
        pokemons.append(pokemon)
    return pokemons

def search_by_id(id):
    pokemons=obtainPokemons()
    pokemon_to_search=None
    for pokemon in pokemons:
        if id==pokemon.id:
            pokemon_to_search=pokemon
            break
    return pokemon_to_search