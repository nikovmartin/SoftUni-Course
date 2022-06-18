# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"
#
# print(palindrome("peter", 0))

def palindrome(word, idx):
    if idx >= len(word) // 2:
        return f"{word} is a palindrome"
    left = word[idx]
    right = word[-1 - idx]
    if left == right:
        return palindrome(word, idx + 1)
    else:
        return f"{word} is not a palindrome"

print(palindrome("gereg", 0))