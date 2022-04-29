words = input().split(" ")
word_count = len(words)

for word in words:
    digit_list = list()
    word_list = list()
    for i in range(len(word)):
        if word[i].isdigit():
            digit_list.append(word[i])
        else:
            word_list.append(word[i])
        first_letter = chr(int("".join(digit_list)))
        rest_letters = "".join(word_list)
        scrambled = first_letter + rest_letters
    scrambled = list(scrambled)
    scrambled[1], scrambled[-1] = scrambled[-1], scrambled[1]
    scrambled = "".join(scrambled)
    print(scrambled, end=" ")

