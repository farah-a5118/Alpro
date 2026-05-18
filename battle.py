import random

def enemy_action(enemies):

    enemy_name = enemies["name"]
    if enemy_name == "Zombie":
        actions = [
        "attack",
        "attack",
        "attack",
        "defend"
    ]

    elif enemy_name == "Skeleton":
        actions = [
        "attack",
        "dodge",
        "attack"
    ]

    elif enemy_name == "Slime":
        actions = [
        "attack",
        "attack",
        "attack"
    ]
        
    elif enemy_name == "Wolf":
        actions = [
        "attack",
        "dodge",
        "defend",
        "attack"
    ]

    elif enemy_name == "Skog":
        actions = [
        "attack",
        "dodge",
        "attack",
        "defend",
        "skill"
    ]

    else:
        actions = [
            "attack"
        ]

    return random.choice(actions)