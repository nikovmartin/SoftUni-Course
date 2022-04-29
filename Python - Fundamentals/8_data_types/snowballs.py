balls_count = int(input())
best_value = 0
# best_weight = 0
# best_time = 0
# best_quality = 0
best_data = ""
for i in range (balls_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > best_value:
        best_value = value
        # best_time = time
        # best_quality = quality
        # best_weight = weight
        best_data = f"{weight} : {time} = {int(value)} ({quality})"
print(best_data)