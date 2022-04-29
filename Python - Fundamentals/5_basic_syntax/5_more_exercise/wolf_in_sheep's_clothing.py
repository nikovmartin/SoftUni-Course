text = input()
split = text.split(", ")
if split[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(split)):
        if split[i] == "wolf":
            sheep_in_danger = len(split) - i - 1
            break
    print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")
