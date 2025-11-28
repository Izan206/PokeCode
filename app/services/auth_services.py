from app.models.exceptions import TrainerNotFound
from app.models.trainer import Trainer

def authenticate(name, password):
    trainer = Trainer.query.filter_by(name=name).first()
    if trainer and trainer.check_password(password):
        return trainer
    raise TrainerNotFound()
