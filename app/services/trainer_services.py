from app.repositories import trainer_repo


def obtain_trainer_by_name(name):
    if name==None or name=="":
        return None
    return trainer_repo.get_trainer_by_name(name)