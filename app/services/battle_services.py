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


def checkHP(hp, damage):
    hp -= damage
    if hp < 0:
        hp = 0
    return hp


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
