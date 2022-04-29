capacity_left = 255
total_intake = 0
n = int(input())
for i in range(n):
    current_pour = int(input())
    if current_pour <= capacity_left:
        capacity_left -= current_pour
        total_intake += current_pour
    else:
        print("Insufficient capacity!")
print(total_intake)