segments = input().split()
total = 0
for segment in segments:
    first_letter = segment[0]
    last_letter = segment[-1]
    number = int(segment[1:-1])
    if first_letter.isupper():
        total += number / (ord(first_letter.lower()) - 96)
    else:
        total += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total -= ord(last_letter.lower()) - 96
    else:
        total += ord(last_letter) - 96
print(f"{total:.2f}")