n = int(input())
list_of_numbers = list()
while n > 0:
    current_number = n % 10
    list_of_numbers.append(current_number)
    n = n // 10
list_of_numbers.sort(reverse=True)
string_ints = [str(int) for int in list_of_numbers]
str_of_ints = "".join(string_ints)
print(str_of_ints)
