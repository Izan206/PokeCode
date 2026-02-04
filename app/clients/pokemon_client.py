import requests
import time
from collections import OrderedDict

TIEMPO_LIMITE = 300 #esto son 5 mins
MAX_CACHE = 50

_cachePokemon = OrderedDict()
_cacheMovements = OrderedDict()
_cachePokemonsPaginados = OrderedDict()

def paginate_pokemons(page):
    if page in _cachePokemonsPaginados:
        data = _cachePokemonsPaginados[page]
        if time.time() - data["expiracion"] < TIEMPO_LIMITE:
            _cachePokemonsPaginados.move_to_end(page)
            return data

    offset = (page-1)*8
    url = f"https://pokeapi.co/api/v2/pokemon?limit=8&offset={offset}"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        data["expiracion"] = time.time()
        _cachePokemonsPaginados[page] = data

        if len(_cachePokemonsPaginados) > MAX_CACHE:
            _cachePokemonsPaginados.popitem(last=False)

        return data
    except Exception:
        return None

def get_pokemons(page):
    data = paginate_pokemons(page)
    if not data:
        return None
    return data["results"]

def get_pokemon_detail(info):
    if info in _cachePokemon:
        data = _cachePokemon[info]
        if time.time() - data["expiracion"] < TIEMPO_LIMITE:
            _cachePokemon.move_to_end(info)
            return data

    url = f"https://pokeapi.co/api/v2/pokemon/{info}"

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        data["expiracion"] = time.time()
        _cachePokemon[info] = data

        if len(_cachePokemon) > MAX_CACHE:
            _cachePokemon.popitem(last=False)

        return data
    except Exception:
        return None

def get_pokemon_attack(url):
    if url in _cacheMovements:
        data = _cacheMovements[url]
        if time.time() - data["expiracion"] < TIEMPO_LIMITE:
            _cacheMovements.move_to_end(url)
            return data

    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()

        data["expiracion"] = time.time()
        _cacheMovements[url] = data

        if len(_cacheMovements) > MAX_CACHE:
            _cacheMovements.popitem(last=False)

        return data
    except Exception:
        return None

def get_all_pokemons_names():
    key = "all_pokemons_list"
    
    if key in _cachePokemonsPaginados:
        data = _cachePokemonsPaginados[key]
        if time.time() - data["expiracion"] < TIEMPO_LIMITE:
            return data

    url = "https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0"
    
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        data["expiracion"] = time.time()
        _cachePokemonsPaginados[key] = data

        if len(_cachePokemonsPaginados) > MAX_CACHE:
            _cachePokemonsPaginados.popitem(last=False)
            
        return data
    except Exception:
        return None