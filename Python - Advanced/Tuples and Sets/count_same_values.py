dict = {}
numbers = [float(x) for x in input().split(" ")]
for number in numbers:
    if number not in dict:
        dict[number] = 0
    dict[number] += 1
# for number in dict:
#     print(f"{number:.1f} - {dict[number]} times")
for number, count in dict.items():
    print(f"{number:.1f} - {count} times")
