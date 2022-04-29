def reverse(x):
    return x[::-1]


while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {reverse(word)}")
