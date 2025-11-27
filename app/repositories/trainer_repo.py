from app.database.db import db
from app.models.trainer import Trainer

def add_trainer(name, password):
    trainer = Trainer(name, password)
    db.session.add(trainer)
    db.session.commit()
    return trainer

def get_trainer_by_name(name):
    trainer = Trainer.query.filter_by(name=name).first()
    return trainer

def obtain_all_trainers():
    trainers=Trainer.query.all()
    return trainers

def get_trainer_by_id(id):
    trainer = Trainer.query.filter_by(id=id).first()
    return trainer

def add_win(id):
    trainer = get_trainer_by_id(id)
    wins = trainer.wins + 1
    trainer.wins = wins
    db.session.commit()
    
def add_lose(id): 
    trainer = get_trainer_by_id(id)
    loses = trainer.loses + 1
    trainer.loses = loses
    db.session.commit()
    
