from flask import Flask, session
from flask_session import Session
from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.battle_routes import battle_bp

app = Flask(__name__)
app.debug = True   # Activate debug mode
app.secret_key = "clave23"

app.config["SESSION_TYPE"] = "filesystem" 
app.config["SESSION_PERMANENT"] = False  
app.config["SESSION_FILE_DIR"] = "./.flask_session" 



Session(app)

app.register_blueprint(home_bp, url_prefix="/")
app.register_blueprint(pokemon_bp, url_prefix="/pokedex")
app.register_blueprint(battle_bp, url_prefix="/battles")

if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
