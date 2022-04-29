n = int(input())
rarity_dict = dict()
for _ in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = plant_info[1]
    rarity_dict[plant] = dict()
    rarity_dict[plant]["rarity"] = rarity
    rarity_dict[plant]["ratings"] = 0
    rarity_dict[plant]["counter"] = 0
while True:
    command = input().split(": ")
    if command[0] == "Exhibition":
        break
    to_do = command[1].split(" - ")
    plant = to_do[0]
    if plant not in rarity_dict:
        print("error")
    else:
        if command[0] == "Rate":
            rating = int(to_do[1])
            rarity_dict[plant]["ratings"] += rating
            rarity_dict[plant]["counter"] += 1
        elif command[0] == "Update":
            new_rarity = to_do[1]
            rarity_dict[plant]["rarity"] = new_rarity
        elif command[0] == "Reset":
            rarity_dict[plant]["ratings"] = 0
            rarity_dict[plant]["counter"] = 0
print("Plants for the exhibition:")
for rare in rarity_dict:
    if rarity_dict[rare]["counter"] == 0:
        average_rating = f"{0:.2f}"
    else:
        average_rating = rarity_dict[rare]["ratings"] / rarity_dict[rare]["counter"]
        average_rating = f"{average_rating:.2f}"
    print(f"- {rare}; Rarity: {rarity_dict[rare]['rarity']}; Rating: {average_rating}")
