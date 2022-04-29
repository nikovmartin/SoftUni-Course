string = input()
digits = ""
letters = ""
chars = ""
for i in string:
    if i.isdigit():
        digits += i
    elif ord(i) in range(65, 90) or ord(i) in range(97, 122):
        letters += i
    else:
        chars += i
print(digits)
print(letters)
print(chars)