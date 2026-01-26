import json
from pathlib import Path
from app.models.pokemon import Pokemon

DATA_PATH=Path(__file__).parent.parent.parent / "data" / "pokemon.json"

with open(DATA_PATH, encoding="utf-8") as f:
    _POKEMONS = json.load(f)
    
def obtain_pokemons():
    pokemons=[]
    for p in _POKEMONS:
        pokemon=Pokemon(**p)
        pokemons.append(pokemon)
    return pokemons

def search_by_id(id):
    pokemons=obtain_pokemons()
    pokemon_to_search=None
    for pokemon in pokemons:
        if id==pokemon.id:
            pokemon_to_search=pokemon
            break
    return pokemon_to_search
