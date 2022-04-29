fires = input().split("#")
water = int(input())
current_level = 0
effort = 0
total_fire = 0
high_range = [x for x in range(81, 126)]
med_range = [x for x in range(51, 81)]
low_range = [x for x in range(1, 51)]
print("Cells:")
for fire in fires:
    if "High" in fire:
        current_level = fire.removeprefix("High = ")
        current_level = int(current_level)
        if current_level in high_range:
            if water >= current_level:
                water -= current_level
                effort += 0.25 * current_level
                total_fire += current_level
                print(f"- {current_level}")
    elif "Medium" in fire:
        current_level = fire.removeprefix("Medium = ")
        current_level = int(current_level)
        if current_level in med_range:
            if water >= current_level:
                water -= current_level
                effort += 0.25 * current_level
                total_fire += current_level
                print(f"- {current_level}")
    elif "Low" in fire:
        current_level = fire.removeprefix("Low = ")
        current_level = int(current_level)
        if current_level in low_range:
            if water >= current_level:
                water -= current_level
                effort += 0.25 * current_level
                total_fire += current_level
                print(f"- {current_level}")
print(F"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")