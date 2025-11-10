from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class trainerForm(FlaskForm):
    trainer = StringField("")


class BuscarProductoForm(FlaskForm):
    nombre = StringField("Introduce el nombre del entrenador", validators=[
        DataRequired(message="El campo no puede estar vacio"),
        Length(min=3, max=15, message="El campo debe teer entre 3 y 15 caracteres")
    ]
    )

    # def __init__(self, pokemon_list, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     if pokemon_list:
    #         lista_choices = []
    #         for p in pokemon_list:
    #             par = (p.id, p.name)
    #             lista_choices.append(par)
