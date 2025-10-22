from pathlib import Path
import json
from flask import Flask, abort, current_app, render_template, request, redirect, url_for
from datetime import datetime
import random

app = Flask(__name__)
app.debug = True   # Activate debug mode

current_year = datetime.now().year


with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)


@app.route('/')  # Welcome
def index():
    return render_template('index.html', music="static/sounds/inicio.mp3", current_year=current_year)


@app.route('/trainer', methods=["POST"])
def trainer():
    trainer = request.form.get("trainer")

    if (len(trainer) < 3 or len(trainer) > 15):
        return render_template("index.html", error="The username must have a minimum of 3 characters and a maximum of 15.")
    else:
        return redirect(url_for("pokedex", trainer=trainer))


@app.route('/pokedex')  # Pokemons list
def pokedex():
    trainer = request.args.get('trainer')
    pokemon_list = current_app.config["DATA"]
    mensaje_error = request.args.get("mensaje_error")
    return render_template('pokedex.html',  pokemon_list=pokemon_list, current_year=current_year, trainer=trainer, mensaje_error=mensaje_error)


@app.route('/404')
def error404():
    return render_template('404.html')


@app.route("/pokedex/<int:pokemon_id>")
def pokemon_details(pokemon_id):
    trainer = request.args.get('trainer')
    pokemon_list = current_app.config["DATA"]
    pokemon = None
    for p in pokemon_list:
        if p['id'] == pokemon_id:
            pokemon = p
    if pokemon == None:
        return render_template("404.html")
    return render_template("pokemon_details.html", pokemon=pokemon, trainer=trainer)


@app.route('/pokemon_selected', methods=["POST"])
def pokemon_selected():
    trainer = request.args.get('trainer')
    pokemon_selected = request.form.get('search')
    pokemon_list = current_app.config["DATA"]

    for p in pokemon_list:
        if p['name'] == pokemon_selected.lower():
            return redirect(url_for('battles', pokemon_selected=pokemon_selected))
    
    mensaje_error = "Pokémon not found, please enter the name correctly"
    return redirect(url_for("pokedex", trainer=trainer, mensaje_error = mensaje_error))


@app.route('/battles')
def battles():
    pokemon_selected = request.args.get('pokemon_selected')
    pokemon_list = current_app.config["DATA"]
    pokemon = None
    for p in pokemon_list:
        if p['name'] == pokemon_selected:
            pokemon = p
    #get 4 randoms moves
    all_moves = pokemon["moves"]
    moves = random.sample(all_moves, 4)

    #get a random pokemon to fight
    random_pokemon = random.choice(pokemon_list)

    return render_template("battles.html", pokemon = pokemon, moves = moves, random_pokemon = random_pokemon)

    

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
