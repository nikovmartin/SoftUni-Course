data = input().split(" ")
search = input().split(" ")
availability = dict()

for x in range (0, len(data), 2):
    key = data[x]
    value = data[x + 1]
    availability[key] = value

for i in search:
    if i in availability.keys():
        print(f"We have {availability[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
