products_dict = {}
command = input().split(" ")
while command[0] != "buy":
    product = command[0]
    price = float(command[1])
    qty = int(command[2])
    if product not in products_dict:
        products_dict[product] = [price, qty]
    else:
        products_dict[product] = [price, qty + products_dict[product][1]]
    command = input().split(" ")
for product in products_dict:
    total = products_dict[product][1] * products_dict[product][0]
    print(f"{product} -> {total:.2f}")