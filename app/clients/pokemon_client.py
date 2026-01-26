from concurrent.futures import ThreadPoolExecutor
import time
import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
urlDetail = "https://pokeapi.co/api/v2/pokemon/"

_cachePokemon = {}
_cacheMovements = {}


def get_data(url):
    response = requests.get(url)
    if not response:
        return None
    return response.json()


def get_pokemons():
    data = get_data(url)
    if not data:
        return None
    pokemons = data["results"]
    return pokemons


def get_pokemon_detail(info):
    if info in _cachePokemon:
        print(info)
        return _cachePokemon[info]

    url = f"https://pokeapi.co/api/v2/pokemon/{info}"

    resp = requests.get(url, timeout=5)

    resp.raise_for_status()
    data = resp.json()

    _cachePokemon[info] = data
    return data

    # urlPokemon=urlDetail+f'{info}/'
    # pokemonDetails=get_data(urlPokemon)
    # return pokemonDetails


def get_pokemon_attack(url):
    if url in _cacheMovements:
        return _cacheMovements[url]

    resp = requests.get(url, timeout=5)

    resp.raise_for_status()
    data = resp.json()

    _cacheMovements[url] = data
    return data
    # urlPokemonAttack=url
    # pokemonAttack=get_data(urlPokemonAttack)
    # return pokemonAttack


if __name__ == "__main__":
    data = get_data(url)
    print(data)

    listaPokemons = get_pokemons()
    print(listaPokemons)

    pokemonDetalles = get_pokemon_detail(1)
    print(pokemonDetalles)

# urls=[
#     "https://pokeapi.co/api/v2/pokemon/1/",
#     "https://pokeapi.co/api/v2/pokemon/2/",
#     "https://pokeapi.co/api/v2/pokemon/3/",
#     "https://pokeapi.co/api/v2/pokemon/4/",
#     "https://pokeapi.co/api/v2/pokemon/5/"
# ]


# def fetch_pokemon_detail(url):
#     response=requests.get(url)

#     return response.json()

# def fetch_pokemons_parallel(urls):
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         return list(executor.map(fetch_pokemon_detail, urls))

# pokemons=[]
# for url in urls:
#     pokemons.append(fetch_pokemon_detail(url))

# start=time.perf_counter()
# pokemons=fetch_pokemons_parallel(urls)
# end=time.perf_counter()
# print(f"Tiempo: {end-start:.4f} segundos")

# for pokemon in pokemons:
#     print(pokemon["name"])

# response=fetch_pokemon_detail("https://pokeapi.co/api/v2/pokemon/1/")
# print(response)

# https://pokeapi.co/api/v2/pokemon/1/
