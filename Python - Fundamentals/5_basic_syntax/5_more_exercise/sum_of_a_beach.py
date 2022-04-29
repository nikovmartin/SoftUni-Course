# string = input().lower()
# counter = 0
# my_list = ["sand", "water", "fish", "sun"]
# for item in my_list:
#     if item in my_list:
#         word_count_txt = string.count(item)
#         counter += word_count_txt
# print(counter)

# text = input().lower()
# counter = 0
# # my_list = ["sand", "water", "fish", "sun"]
# counter += text.count("sand")
# counter += text.count("water")
# counter += text.count("fish")
# counter += text.count("sun")
# print(counter)

text = input().lower()
counter = 0
my_list = ["sand", "water", "fish", "sun"]
for word in range(len(my_list)):
    counter += text.count(my_list[word])
print(counter)