# command = input()
# coffee_counter = 0
#
# while command != "END":
#     if command == "coding" or command == "dog" or command == "cat" or command == "movie":
#         coffee_counter += 1
#     elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
#         coffee_counter += 2
#     else:
#         coffee_counter += 0
#     command = input()
# if coffee_counter > 5:
#     print("You need extra sleep")
# else:
#     print(coffee_counter)

command = input()
coffee_counter = 0
lowercase = ["coding", "dog", "cat", "movie"]
uppercase = ["CODING", "DOG", "CAT", "MOVIE"]

while command != "END":
    if command in lowercase:
        coffee_counter += 1
    elif command in uppercase:
        coffee_counter += 2
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)