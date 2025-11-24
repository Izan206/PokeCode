
from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash


class Trainer(db.Model):
    __tablename__ = "trainer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("La contraseña no puede leerse.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def authenticate(name, password):
        trainer = name.query.filter_by(name=name).first()

        if trainer and trainer.verify_password(password):
            return trainer 
        return None
