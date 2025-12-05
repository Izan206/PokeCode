from app.database.db import db
from app.models.trainer import Trainer


def add_trainer(name, password, skin):
    trainer = Trainer(name=name, password=password, skin=skin)
    db.session.add(trainer)
    db.session.commit()
    return trainer


def get_trainer_by_name(name):
    trainer = Trainer.query.filter_by(name=name).first()
    return trainer


def obtain_all_trainers():
    trainers = Trainer.query.all()
    return trainers


def get_trainer_by_id(id):
    trainer = Trainer.query.filter_by(id=id).first()
    return trainer


def add_win(trainer):
    trainer.wins += 1
    db.session.commit()


def add_lose(trainer):
    trainer.loses += 1
    db.session.commit()


def add_exp(trainer, exp):
    trainer.exp += exp
    db.session.commit()
