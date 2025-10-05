from pathlib import Path
import json
from flask import Flask, current_app, jsonify, render_template

app = Flask(__name__)

with open(Path("data\pokemon.json"), "r", encoding="utf-8") as f:
    app.config["DATA"]=json.load(f)
    
@app.route('/')
def index():
    return render_template('index.html', music="static/sounds/inicio.mp3")

@app.route('/pokemons')
def pokemons():
    return jsonify(current_app.config["DATA"]) 

@app.route('/battle')
def battle():
    return render_template("battle.html", music="static/sounds/battle.mp3")

if __name__=='__main__':
    app.run('0.0.0.0', 8080)