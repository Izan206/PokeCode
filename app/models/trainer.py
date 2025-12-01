
from app.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class Trainer(db.Model):
    __tablename__ = "trainer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, nullable=False, default=0)
    loses = db.Column(db.Integer, nullable=False, default=0)
    exp = db.Column(db.Integer, nullable=False, default=1)
    skin = db.Column(db.String, nullable=False)

    def __init__(self, name, password, skin, wins=0, loses=0, exp=1):
        self.name = name
        self.password = generate_password_hash(password)
        self.skin = skin
        self.wins = wins
        self.loses = loses
        self.exp = exp

    def check_password(self, password_introduced):
        return check_password_hash(self.password, password_introduced)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "wins": self.wins,
            "loses": self.loses,
            "exp": self.exp
        }
