words = input().split(" ")
palindrome_list = list()
palindrome = input()
for word in words:
    if "".join(reversed(word)) == word:
        palindrome_list.append(word)
print(palindrome_list)
count = palindrome_list.count(palindrome)
print(f"Found palindrome {count} times")

