#capa intermedia que contiene la logica de negocio y hace llamada a funciones
import app.repositories.pokemon_repo as pokemon_repo


def list_pokemons():
    return pokemon_repo.obtainPokemons()

def obtain_pokemon_by_id(id):
    if id<0 or id is None:
        return None
    return pokemon_repo.search_by_id(id)
    
def obtain_pokemon_by_name(name):
    pokemons=list_pokemons()
    pokemon=None
    for p in pokemons:
        if p.name==name:
            pokemon=p
            break
        
    return pokemon