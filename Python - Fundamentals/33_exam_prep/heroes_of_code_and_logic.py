count = int(input())
heroes = dict()

for i in range(count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hp = int(current_hero[1])
    mp = int(current_hero[2])
    current_hero_dict = dict()
    current_hero_dict["HP"] = hp
    current_hero_dict["MP"] = mp
    heroes[hero_name] = current_hero_dict
# a hero can have a maximum of 100 HP and 200 MP
while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    hero_name = command[1]
    value = int(command[2])
    if command[0] == "CastSpell":
        spell_name = command[3]
        if heroes[hero_name]["MP"] - value >= 0:
            heroes[hero_name]["MP"] -= value
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        attacker = command[3]
        if heroes[hero_name]["HP"] - value > 0:
            heroes[hero_name]["HP"] -= value
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command[0] == "Recharge":
        if heroes[hero_name]["MP"] + value > 200:
            value = 200 - heroes[hero_name]["MP"]
        heroes[hero_name]["MP"] += value
        print(f"{hero_name} recharged for {value} MP!")
    elif command[0] == "Heal":
        if heroes[hero_name]["HP"] + value > 100:
            value = 100 - heroes[hero_name]["HP"]
        heroes[hero_name]["HP"] += value
        print(f"{hero_name} healed for {value} HP!")

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")