import os
from flask import Flask
from flask_session import Session
from app.database.db import db
from app.routes.home_routes import home_bp
from app.routes.pokemon_routes import pokemon_bp
from app.routes.battle_routes import battle_bp
from app.models.trainer import Trainer

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

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
db_path = os.path.join(BASE_DIR, "data", "pokemons.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.cli.command("create-tables")
def create_table():
    print("Creating tables")
    db.drop_all()
    db.create_all()
    print("Tables created")
# @app.route("/test")
# def test():
#     nombre="Izan"
#     password="1234"
#     usuario=Usuario.query.get(id)
#     esPasswordValida=usuario.check_password(password)
#     db.session.add(usuario)
#     db.session.commit()

#     return esPasswordValida


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
