from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class PokemonForm(FlaskForm):
    pokemons = SelectField("Selecciona el pokemon", choices=[], coerce=int)
    enviar = SubmitField("Buscar: ")
    
    def __init__(self, pokemons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if pokemons:
            lista_choices=[]
            for p in pokemons:
                par=(p.id, p.nombre)
                lista_choices.append(par)
            
            self.pokemons.choices = lista_choices