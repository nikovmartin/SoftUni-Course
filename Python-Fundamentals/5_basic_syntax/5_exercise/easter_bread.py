budget = float(input())
price_1kg_flour = float(input())
price_pack_eggs = 0.75 * price_1kg_flour
price_of_milk_for_one_bread = 1.25 * price_1kg_flour * 0.25
price_per_bread = price_of_milk_for_one_bread + price_pack_eggs + price_1kg_flour
bread_count = 0
colored_eggs = 0
while budget > 0:
    if budget - price_per_bread < 0:
        break
    budget -= price_per_bread
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2
print(f"You made {bread_count} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
