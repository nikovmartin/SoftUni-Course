num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


result = subtract(sum_numbers(num_1, num_2), num_3)
print(result)