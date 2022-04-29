text = input()
final_text = ""
final_text += text[0]
for i in range(len(text) -1):
    current = text[i]
    next = text[i+1]
    if current != next:
        final_text += next
print(final_text)