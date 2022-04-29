n = int(input())
n = 2 * n
synonyms = {}
for i in range(0, n, 2):
    word = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(input())

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
