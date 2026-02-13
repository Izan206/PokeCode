from app.clients.pokemon_client import get_pokemon_attack, get_pokemons, get_pokemon_detail


def list_pokemons(num):
    listPokemons = get_pokemons(num)
    listPokemonsAdapted = []
    if listPokemons is None:
        return None

    for pokemon in listPokemons:
        name = pokemon["name"]
        pokemonAdapted = adapt_data_pokemon(name)
        if pokemonAdapted:
            listPokemonsAdapted.append(pokemonAdapted)

    return listPokemonsAdapted


def get_data_pokemon_atack(move):
    name = ""
    url = ""
    accuracy = 0
    power = 0
    type = ""
    name = move["move"]["name"]
    url = move["move"]["url"]

    attack = get_pokemon_attack(url)
    accuracy = attack["accuracy"]
    power = attack["power"]
    type = attack["type"]["name"]

    ataqueAdaptado = {
        "name": name,
        "url": url,
        "accuracy": accuracy,
        "power": power,
        "type": type
    }
    return ataqueAdaptado


def adapt_data_pokemon(id):
    pokemonData = get_pokemon_detail(id)
    
    if pokemonData is None:
        return None

    contadorMovimientos = 0
    movementsList = []
    for move in pokemonData["moves"]:
        contadorMovimientos += 1
        if contadorMovimientos <= 6:
            moveAdapted = get_data_pokemon_atack(move)
            movementsList.append(moveAdapted)
        else:
            break

    sprites_data = {
        "front_default": pokemonData["sprites"].get("front_default"),
        "back_default": pokemonData["sprites"].get("back_default"),
        "front_shiny": pokemonData["sprites"].get("front_shiny"),
        "back_shiny": pokemonData["sprites"].get("back_shiny")
    }

    name = ""
    value = 0
    statsList = []
    for i in pokemonData["stats"]:
        value = i["base_stat"]
        name = i["stat"]["name"]
        objetoStat = {
            "name": name,
            "value": value
        }
        statsList.append(objetoStat)

    listTypes = []
    contadorTipo = 0
    for i in pokemonData["types"]:
        if contadorTipo <= 2:
            type = i["type"]["name"]
            listTypes.append(type)

    pokemonAdaptado = {
        "id": pokemonData["id"],
        "name": pokemonData["name"],
        "height": pokemonData["height"],
        "weight": pokemonData["weight"],
        "stats": statsList,
        "sprites": sprites_data,
        "moves": movementsList,
        "types": listTypes
    }
    return pokemonAdaptado


def obtain_pokemon_by_id(id):
    if id < 0 or id is None:
        return None
    pokemon = adapt_data_pokemon(id)
    return pokemon


def obtain_pokemon_by_name(name):
    if not name:
        return None
    pokemonAdapted = adapt_data_pokemon(name)
    return pokemonAdapted
