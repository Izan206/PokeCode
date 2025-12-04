from app.database.db import db

class Participates(db.Model):
    __tablename__="participates"
    
    id=db.Column(db.Integer, primary_key=True)
    trainer_id=db.Column(db.Integer, db.ForeignKey("trainer.id"), nullable=False)
    battle_id=db.Column(db.Integer, db.ForeignKey("battle_db.id"), nullable=False)
    
    trainer=db.relationship("Trainer", back_populates="participates")
    battle_db=db.relationship("Battle_db", back_populates="participates")
    
