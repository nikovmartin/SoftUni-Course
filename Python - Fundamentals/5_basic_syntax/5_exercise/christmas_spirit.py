cost = 0
christmas_spirit = 0
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15
qty = int(input())
days = int(input())

for i in range (1,days+1):
    if i % 11 == 0:
        qty += 2
    if i % 2 == 0:
        cost += qty * price_ornament_set
        christmas_spirit += 5
    if i % 3 == 0:
        cost += qty * price_tree_garlands + qty * price_tree_skirt
        christmas_spirit += 13
    if i % 5 == 0:
        cost += qty * price_tree_lights
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        cost += price_tree_lights + price_tree_skirt + price_tree_garlands
        if i == days:
            christmas_spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")