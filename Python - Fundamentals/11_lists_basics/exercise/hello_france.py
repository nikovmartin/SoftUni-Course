collection_items = input().split("|")
budget = float(input())
list_sold_price = list()
profit = 0
total_sold = 0
condition = False
for data_items in collection_items:
    current_item = data_items.split("->")
    item = current_item[0]
    price_bought = float(current_item[1])
    condition = False
    if item == "Clothes":
        if price_bought <= 50:
            condition = True
    elif item == "Shoes":
        if price_bought <= 35:
            condition = True
    elif item == "Accessories":
        if price_bought <= 20.50:
            condition = True
    if condition is True:
        if budget >= price_bought:
            budget -= price_bought
            profit += price_bought * 0.4
            price_sold = price_bought * 1.4
            total_sold += price_sold
            list_sold_price.append(f"{price_sold:.2f}")

print(" ".join(list_sold_price))
print(f"Profit: {profit:.2f}")
if (total_sold + budget) > 150:
    print("Hello, France!")
else:
    print("Not enough money.")