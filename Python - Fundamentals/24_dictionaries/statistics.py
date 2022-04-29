stats = {}
pair = input()
while pair != "statistics":
    pair = pair.split(": ")
    key = pair[0]
    value = int(pair[1])
    if key in stats:
        stats[key] += value
    else:
        stats[key] = value
    pair = input()
print("Products in stock:")
for x in stats.keys():
    print(f"- {x}: {stats[x]}")
print(f"Total Products: {len(stats.keys())}")
print(f"Total Quantity: {sum(stats.values())}")
