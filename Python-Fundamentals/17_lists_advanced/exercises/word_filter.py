# text = input().split(" ")
# even_text = list(filter(lambda word: len(word) % 2 == 0, text))
# for word in even_text:
#     print(word)

text = input().split(" ")
even_text = list(filter(lambda word: len(word) % 2 == 0, text))
print("\n".join(even_text))
