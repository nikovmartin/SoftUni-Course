# n = int(input())
# word = input()
# list_words = list()
# list_including_word = list()
# for i in range(n):
#     list_words.append(input())
# print(list_words)
# for y in range(len(list_words)):
#     if word in list_words[y]:
#         list_including_word.append(list_words[y])
# print(list_including_word)

n = int(input())
word = input()
list_words = list()
list_including_word = list()
for i in range(n):
    current_string = input()
    list_words.append(current_string)
    if word in current_string:
        list_including_word.append(current_string)
print(list_words)
print(list_including_word)


