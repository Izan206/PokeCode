import random

def getMove(pokemon, move_name):
    for move in pokemon.moves:
        if move["name"] == move_name:
            return move
    return


def getLife(pokemon):
    for stat in pokemon.stats:
        if stat["name"] == "hp":
            return stat["value"]


def calculateDamage(attacker, defender, move):
    m_name = move["name"]
    m_power = move["power"]
    m_accuracy = move["accuracy"]

    if m_power is None or m_accuracy is None:
        return 0, f"{attacker.name} used {m_name} but it had no effect."

    # fallo según accuracy
    if random.randint(1, 100) > m_accuracy:
        return 0, f"{attacker.name} used {m_name}, but it missed!"

    defender_hp = getLife(defender)
    # Daño en proporción a la vida del adversario
    base_damage = (m_power / 100) * defender_hp / 4
    # Factor aleatorio para que varie un poco el daño
    random_factor = random.uniform(0.85, 1.15)
    damage = int(max(5, base_damage * random_factor))
    log_message = f"{attacker.name} used {m_name}. It hit {damage} of damage!"
    return damage, log_message

def apply_damage(battle_health, damage):
    battle_health-=damage
    if battle_health<0:
        battle_health=0
    
    is_ko=False
    if battle_health==0:
        is_ko=True
    
    return battle_health, is_ko 
        
    
def get_battle_result(battle):
    if battle.player_health <= 0:
        winner = battle.enemy_pokemon_data.name
        loser = battle.player_pokemon_data.name
    else:
        winner = battle.player_pokemon_data.name
        loser = battle.enemy_pokemon_data.name
    return winner, loser
