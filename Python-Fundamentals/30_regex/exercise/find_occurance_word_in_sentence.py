import re
text = input()
search_word = input()
output = re.findall(rf"\b{search_word}\b", text, re.IGNORECASE)
print(len(output))