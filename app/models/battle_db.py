from app.database.db import db
from datetime import datetime
class Battle_db(db.Model):
    __tablename__="battle_db"
    id=db.Column(db.Integer, primary_key=True)
    trainer_1 = db.Column(db.String, nullable=False)
    trainer_2 = db.Column(db.String, nullable=False)
    pokemon_1 = db.Column(db.String, nullable=False)
    pokemon_2 = db.Column(db.String, nullable=False)
    date=db.Column(db.DateTime, default=datetime.now, nullable=False)
    winner = db.Column(db.String, nullable=False)
    loser = db.Column(db.String, nullable=False)
    
    participates=db.relationship("Participates", back_populates="battle_db")
    
    