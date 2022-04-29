neighbourhood = list(map(int, input().split("@")))
index = 0
while True:
    command = input().split(" ")
    jump = command[0]
    if jump == "Love!":
        break
    index += int(command[1])
    if index >= len(neighbourhood):
        index = 0
    if neighbourhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighbourhood[index] -= 2
        if neighbourhood[index] == 0:
            print(f"Place {index} has Valentine's day.")

print(f"Cupid's last position was {index}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    unsuccessful = len(neighbourhood) - neighbourhood.count(0)
    print(f"Cupid has failed {unsuccessful} places.")
