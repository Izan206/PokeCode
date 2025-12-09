from app.database.db import db
from app.models.battle_db import Battle_db

def create_battle(battle):
    db.session.add(battle)
    db.session.commit()

def get_battle_by_id(id):
    battle=Battle_db.query.filter_by(id=id).first()
    return battle

def get_battle_by_trainer(trainer):
    battles=Battle_db.query.filter_by(trainer_1=trainer).all()
    return battles

def delete_battle(battle):
    db.session.delete(battle)
    db.session.commit()
