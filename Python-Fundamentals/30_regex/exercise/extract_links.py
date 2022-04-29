import re
output = list()
while True:
    text = input()
    if not text:
        break
    expression = r"[w]{3}[.][a-zA-Z\d\-]+[.][a-z]+([.][a-z]+)*"
    websites = re.finditer(expression, text)
    for website in websites:
        output.append(website.group())
print("\n".join(output))