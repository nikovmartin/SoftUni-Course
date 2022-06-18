from collections import deque
chocolates = deque([int(x) for x in input().split(", ")])
milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0
while milkshakes < 5 and milk and chocolates:
    if chocolates[-1] <= 0 and milk[0] <= 0:
        chocolates.pop()
        milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolates[-1] == milk[0]:
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        chocolates[-1] -= 5
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")