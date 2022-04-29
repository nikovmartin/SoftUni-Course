a = input()
b = input()
while a in b:
    b = b.replace(a, "")
print(b)

