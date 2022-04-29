fires = input().split("#")
water = int(input())
current_level = 0
effort = 0
total_fire = 0
high_range = [x for x in range(81, 126)]
med_range = [x for x in range(51, 81)]
low_range = [x for x in range(1, 51)]
condition = False
print("Cells:")
for fire in fires:
    fire_info = fire.split(" = ")
    fire_type = fire_info[0]
    current_level = int(fire_info[1])
    condition = False
    if fire_type == "High":
        if current_level in high_range:
            if water >= current_level:
                condition = True
    elif fire_type == "Medium":
        if current_level in med_range:
            if water >= current_level:
                condition = True
    elif fire_type == "Low":
        if current_level in low_range:
            if water >= current_level:
                condition = True
    if condition is True:
        water -= current_level
        effort += 0.25 * current_level
        total_fire += current_level
        print(f"- {current_level}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")