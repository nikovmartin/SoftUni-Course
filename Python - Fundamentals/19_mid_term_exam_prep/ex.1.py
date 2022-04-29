total_price = 0
tax = 1.2
discount = 0.9
while True:
    price = input()
    if price == "special" or price == "regular":
        total_taxed_price = total_price * tax
        taxes = total_taxed_price - total_price
        if total_price == 0:
            print("Invalid order!")
            break
        else:
            if price == "special":
                total_taxed_price = total_taxed_price * discount
            print("Congratulations you've just bought a new computer!\n"
                  f"Price without taxes: {total_price:.2f}$\n"
                  f"Taxes: {taxes:.2f}$\n"
                  "-----------\n"
                  f"Total price: {total_taxed_price:.2f}$")
            break
    if float(price) <= 0:
        print("Invalid price!")
        continue
    else:
        total_price += float(price)


