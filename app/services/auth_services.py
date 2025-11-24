from functools import wraps
from flask import redirect, session, url_for


def required_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "trainer" not in session:
            return redirect(url_for("home.index"))
        return func(*args, **kwargs)
    return wrapper


def authenticate(name, password):
    trainer = name.query.filter_by(name=name).first()
    if trainer and trainer.check_password(password):
        return trainer
    return None
