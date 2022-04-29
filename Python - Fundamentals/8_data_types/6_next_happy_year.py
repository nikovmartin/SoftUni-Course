number = int(input())
happy_year = False
while not happy_year:
    number += 1
    str_number = str(number)
    set_number = set(str_number)
    if len(set_number) == len(str_number):
        happy_year = True
print(number)