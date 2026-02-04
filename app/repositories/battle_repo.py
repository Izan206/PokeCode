from app.database.db import db
from app.models.battle_db import Battle_db
from app.models.participates import Participates

def create_battle(battle, trainer_id):
    db.session.add(battle)
    db.session.commit()
    
    participacion = Participates(
        trainer_id=trainer_id,
        battle_id=battle.id 
    )
    db.session.add(participacion)
    db.session.commit()
    return battle

def get_battle_by_id(id):
    battle=Battle_db.query.filter_by(id=id).first()
    return battle

def get_battles_by_trainer(trainer):
    battles=Battle_db.query.filter_by(trainer_1=trainer).all()
    return battles

def delete_battle(battle_id):
    battle_to_delete = get_battle_by_id(battle_id)
    if battle_to_delete:
        for p in battle_to_delete.participates:
            db.session.delete(p)

        db.session.delete(battle_to_delete)
        db.session.commit()


# SELECT e.nombre, d.nombre
# FROM empleados e
# INNER JOIN asignaciones a ON e.id=a.empleado_id
# INNER JOIN departamentos d ON d.id=a.departamento_id
# WHERE a.cargo="Jefe";

# ==

# resultado=db.session.query(Empleado).join(Asignacion).join(Departamento).filter(Asignacion.cargo=="Jefe")