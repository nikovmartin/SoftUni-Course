current_product = input()
current_qty = int(input())


def order(product,qty):
    if product == "coffee":
        return 1.5 * qty
    elif product == "water":
        return 1 * qty
    elif product == "coke":
        return 1.4 * qty
    elif product == "snacks":
        return 2 * qty


final_price = order(current_product, current_qty)
print(f"{final_price:.2f}")