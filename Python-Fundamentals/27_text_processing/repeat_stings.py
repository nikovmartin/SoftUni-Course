text = input().split(" ")
result = ""
for x in text:
    result += x * len(x)
print(result)