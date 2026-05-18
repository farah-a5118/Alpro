import random
import json
import os
import time

with open('data/class.json', 'r') as f: #FILE HANDLING
    classes = json.load(f)

with open("data/enemies.json", "r") as f: #FILE HANDLING
    enemies = json.load(f)

with open("data/loot.json", "r") as f:
    loots = json.load(f)

print(classes["Mage"]["hp"]) #DICTIONARY

rarity_chances = { #DICTIONARY/HASH TABLE
    "common" : 65,
    "uncommon" : 23,
    "rare" : 7,
    "Legendary" : 5
}

player = { #DICTIONARY/HASH TABLE
    "name": "",
    "class": "",
    "hp": 0,
    "max_hp": 0,
    "att": 0,
    "def": 0,
    "skill": 0,
    "level": 1,
    "exp": 0,
    "inventory": [] #LIST
}

def clear_terminal():
    os.system("cls")

def loading():
    print("\nLoading", end="")

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")

    print()

def choosing():
    clear_terminal()

    print("=== ALL CHARACTERS ===\n")

    for name_class in classes: #LOOPING

        data = classes[name_class]

        print(f"{name_class}")
        print(f"HP      : {data['hp']}")
        print(f"ATK     : {data['atk']}")
        print(f"DEF     : {data['def']}")
        print(f"SKILL   : {data['skill']}")
        print()

    choice = input("Select character: ")

    if choice not in classes: #SEARCHING
        print("\nClass isn't available!")
        time.sleep(1)
        return

    nama = input("Enter player name: ")

    data = classes[choice]

    player["name"] = nama
    player["class"] = choice
    player["hp"] = data["hp"]
    player["max_hp"] = data["hp"]
    player["atk"] = data["atk"]
    player["def"] = data["def"]
    player["skill"] = data["skill"]

    print(f"\nSuccesfully selected {choice}!")
    time.sleep(1)

def stats():
    clear_terminal()

    print("=== PLAYER INFO ===")

    print(f"Name        : {player['name']}")
    print(f"Class       : {player['class']}")
    print(f"HP          : {player['hp']}")
    print(f"ATK         : {player['atk']}")
    print(f"DEF         : {player['def']}")
    print(f"LEVEL       : {player['level']}")
    print(f"EXP         : {player['exp']}")

    print("\nPress ENTER to go back.")

def loot_system():
    roll = random.randint(1, 100) #PROBABILITAS

    if roll <= rarity_chances["legendary"]:
        rarity = "legendary"

    elif roll <= 12:
        rarity = "rare"

    elif roll <= 35:
        rarity = "umcommon"

    else:
        rarity = "common"

    loot = random.choice(loots[rarity])

    player["inventory"].append(loot)

    print(f"\nYou got an item!: ")
    print(f"{loot} [{rarity.upper()}]")

def inventory():
    clear_terminal()

    print("=== INVENTORY ===")
    if len(player["inventory"]) == 0:
        print("Inventory's empty")
    else:
        number = 1

        for item in player["inventory"]:
            print(f"{number}. {item}")
            number += 1

    print("\nPress ENTER to go back.")