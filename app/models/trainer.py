
from app.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class Trainer(db.Model):
    __tablename__ = "trainer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    loses = db.Column(db.Integer, nullable=False)
    

    def __init__(self, name, password, wins=0, loses=0):
        self.name = name
        self.password= generate_password_hash(password)
        self.wins = wins
        self.loses = loses

    def check_password(self, password_introduced):
        return check_password_hash(self.password, password_introduced)
