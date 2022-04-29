import re
n = int(input())
for i in range(n):
    text = input()
    output = "".join(re.findall(r"[@][#]+[A-Z][a-zA-Z0-9]{4,}[A-Z][@][#]+", text))
    if output != "":
        number = "".join(re.findall(r"\d+", output))
        if number != "":
            product_group = number
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
