def validator(text):
    valid = True
    special_chars = False
    number = 0
    letter = 0
    for char in text:
        if 48 <= ord(char) <= 57:
            number += 1
        elif 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            letter += 1
        else:
            special_chars = True
    if len(text) < 6 or len(text) > 10:
        print("Password must be between 6 and 10 characters")
        valid = False
    if special_chars is True:
        print("Password must consist only of letters and digits")
        valid = False
    if number < 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid is True:
        print("Password is valid")


user_password = input()
validator(user_password)
