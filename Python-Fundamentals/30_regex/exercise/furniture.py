import re
furniture = list()
total = 0
while True:
    text = input()
    if text == "Purchase":
        break
    else:
        expression = r"[>]{2}(?P<name>\w+)[<]{2}(?P<price>\d+|\d+\.\d+)[!](?P<qty>\d+)"
        information = re.finditer(expression, text)
        for info in information:
            name = expression
            furniture.append(info.group("name"))
            total += float(info.group("price")) * int(info.group("qty"))

print("Bought furniture:")
if total > 0:
    print("\n".join(furniture))
print(f"Total money spend: {total:.2f}")