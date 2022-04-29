cities = dict()
while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    else:
        city_name = command[0]
        population = int(command[1])
        gold = int(command[2])
        if city_name not in cities:
            cities[city_name] = dict()
            cities[city_name]["population"] = population
            cities[city_name]["gold"] = gold
        else:
            cities[city_name]["population"] += population
            cities[city_name]["gold"] += gold
while True:
    command = input().split("=>")
    if command[0] == "End":
        break
    city_name = command[1]
    if command[0] == "Plunder":
        population = int(command[2])
        gold = int(command[3])
        cities[city_name]["population"] -= population
        cities[city_name]["gold"] -= gold
        print(f"{city_name} plundered! {gold} gold stolen, {population} citizens killed.")
        if cities[city_name]["population"] == 0 or cities[city_name]["gold"] == 0:
            del cities[city_name]
            print(f"{city_name} has been wiped off the map!")
    elif command[0] == "Prosper":
        gold = int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[city_name]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city_name} now has {cities[city_name]['gold']} gold.")
if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")