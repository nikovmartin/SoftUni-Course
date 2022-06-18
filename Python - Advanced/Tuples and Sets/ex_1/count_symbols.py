text = input()
char_counter = {}
for char in text:
    if char not in char_counter:
        char_counter[char] = 0
    char_counter[char] += 1
for char, count in sorted(char_counter.items()):
    print(f"{char}: {count} time/s")