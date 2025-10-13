from pathlib import Path
import json
from flask import Flask, abort, current_app, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.debug = True   # Activate debug mode

current_year = datetime.now().year


with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    app.config["DATA"] = json.load(f)


@app.route('/', methods=["GET", "POST"])  # Welcome
def index():
    return render_template('index.html', music="static/sounds/inicio.mp3", current_year=current_year)

def trainer():
    if request.method=="POST":
        trainer=request.form.get("trainer")
        
        if (len(trainer)<3 or len(trainer)>15):
            return render_template("index.html", error="El usuario debe tener un minimo de 3 caracteres y un maximo de 15")
        else:
            return redirect(url_for("pokedex"))
    


@app.route('/pokedex')  # Pokemons list
def pokedex():
    pokemon_list = current_app.config["DATA"]
    return render_template('pokedex.html',  pokemon_list=pokemon_list, current_year=current_year)


@app.route('/404')
def error404():
    return render_template('404.html')

@app.route("/pokedex/<int:pokemon_id>")
def pokemon_details(pokemon_id):
    pokemon_list=current_app.config["DATA"]
    pokemon=None
    for p in pokemon_list:
        if p['id']==pokemon_id:
            pokemon=p
    if pokemon==None:
            return render_template("404.html")
    return render_template("pokemon_details.html", pokemon=pokemon)


@app.route('/', methods=["GET", "POST"])
def trainer():
    if request.method=="GET":
        return render_template("index.html")
    
    if request.method=="POST":
        user=request.form.get("user")
        password=request.form.get("password")
        
        if (len(user)<3):
            return render_template("index.html", error="El usuario debe tener un minimo de 3 caracteres")
    
        if user and password == "1234":
            return redirect(url_for("pokedex"))
        
        return f"Hola {user} tu contraseña es {password}"
        
if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
