total_price = 0
n = int(input())

for i in range(0,n):
    price_per_capsule = float(input())
    days = int(input())
    qty_capsule = int(input())

    price_current_order = price_per_capsule * days * qty_capsule
    total_price += price_current_order
    print(f"The price for the coffee is: ${price_current_order:.2f}")

print(f"Total: ${total_price:.2f}")