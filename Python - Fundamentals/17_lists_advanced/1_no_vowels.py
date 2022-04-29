vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
no_vowels = "".join([i for i in text if i not in vowels])
print(no_vowels)