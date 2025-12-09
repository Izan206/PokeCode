from app.models import battle_db


class Battle:
    
    def __init__(self, player_pokemon_data, enemy_trainer, enemy_pokemon_data, player_health, enemy_health, player_moves, enemy_moves, log=None, turn=1):
        self.turn = turn
        self.enemy_trainer = enemy_trainer
        self.player_pokemon_data = player_pokemon_data
        self.enemy_pokemon_data = enemy_pokemon_data
        if log is None:
            self.log=[]
        else:
            self.log=log
        self.player_health = player_health
        self.enemy_health = enemy_health
        self.player_moves = player_moves
        self.enemy_moves = enemy_moves