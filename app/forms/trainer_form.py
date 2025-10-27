from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class trainerForm(FlaskForm):
    trainer=StringField("")

class BuscarProductoForm(FlaskForm):
    nombre=StringField("Introduce el nombre del entrenador", validators= [
        DataRequired(message="El campo no puede estar vacio"),
        Length(min=3, max=15, message="El campo debe teer entre 3 y 15 caracteres")
    ]
)