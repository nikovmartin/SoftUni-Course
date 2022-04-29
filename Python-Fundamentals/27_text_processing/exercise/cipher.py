inital_text = input()
final_text = [chr(ord(i) + 3) for i in inital_text]
print("".join(final_text))