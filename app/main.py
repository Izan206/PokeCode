from pathlib import Path
import json
from flask import Flask, current_app, render_template
from datetime import datetime

app = Flask(__name__)
app.debug = True   # Activate debug mode

current_year = datetime.now().year


with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)


@app.route('/')  # Welcome
def index():
    return render_template('index.html', music="static/sounds/inicio.mp3", current_year=current_year)


@app.route('/pokedex')  # Pokemons list
def pokedex():
    pokemon_list = current_app.config["DATA"]
    return render_template('pokedex.html',  pokemon_list=pokemon_list, current_year=current_year)


@app.route('/404')
def error404():
    return render_template('404.html')



# @app.route("/pokedex/<int:id>")
# def pokemon_detail(pokemon_id):
#     pokemon_list=current_app.config('pokemon_list')
#     pokemon=None
#     for p in pokemon_list:
#         if pokemon.id=pokemon_id:
#             pokemon=p
            
#     return render_template("product_details.html", pokemon=pokemon)
            
if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
