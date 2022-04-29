words = input().split(" ")
# words = [word.lower() for word in words]
words = list(map(lambda word: word.lower(), words))
dict_1 = {}
output = []
for word in words:
    if word not in dict_1:
        dict_1[word] = 1
    else:
        dict_1[word] += 1

for word in dict_1.keys():
    if dict_1[word] % 2 != 0:
        output.append(word)

print(" ".join(output))
