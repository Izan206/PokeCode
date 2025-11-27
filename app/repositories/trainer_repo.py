from app.database.db import db
from app.models.trainer import Trainer


def add_trainer(name, password):
    trainer = Trainer(name, password)
    db.session.add(trainer)
    db.session.commit()


def get_trainer_by_name(name):
    trainer = Trainer.query.filter_by(name=name).first()
    return trainer

def obtain_all_trainers():
    trainers=Trainer.query.all()
    return trainers