from app.models.exceptions import TrainerNotFound
from app.models.trainer import Trainer
from app.services.trainer_services import obtain_trainer_by_name

def authenticate(name, password):
    trainer = obtain_trainer_by_name(name)
    if trainer and trainer.check_password(password):
        return trainer
    raise TrainerNotFound()
