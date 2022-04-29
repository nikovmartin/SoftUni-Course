data = input().upper()
unique_letters = []
string = ""
number = ""
output = ""
for letter in data:
    if letter not in unique_letters and letter.isdigit() is False:
        unique_letters.append(letter)
print(f"Unique symbols used: {len(unique_letters)}")

for i in range(len(data)):
    if data[i].isdigit() is False:
        string += data[i]
    else:
        if i != len(data) - 1:
            if data[i+1].isdigit():
                number += data[i]
                number += data[i+1]
            else:
                number = data[i]
        else:
            number = data[i]
        string *= int(number)
        output += string
        string = ""
        number = ""

print(output)