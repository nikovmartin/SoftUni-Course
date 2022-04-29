import sys
a = int(input())
b = int(input())
c = int(input())
highest_number = -sys.maxsize
if a > highest_number:
    highest_number = a
if b > highest_number:
    highest_number = b
if c > highest_number:
    highest_number = c
print(highest_number)