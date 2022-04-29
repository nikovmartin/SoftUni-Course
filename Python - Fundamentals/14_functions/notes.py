#1
print()
type()
input()
abs()
pow()
dir()
sorted()
max()

#2
def test():
    print(10 * 10)

test()

#3
def test(a, b):
    print(a * b)

test(10, 10)

#4
def test(a, b):
    print(a / b)


test(b=10, a=2)


#5
def name(first_name="Martin", last_name="Nikov"):
    print(f"Hello {first_name} {last_name}")


print(name)

#6
def test(a, b):
    return(a * b)


num_1 = int(input())
num_2 = int(input())

print(test(num_1, num_2))

#7
def test(a, b):
    return a * b


def total_numbers(c):
    result = test(5, 5) * c
    return result


current_number = int(input())
print(total_numbers(current_number))


#8
x = lambda a, b: a * b
print(x(2, 3))
