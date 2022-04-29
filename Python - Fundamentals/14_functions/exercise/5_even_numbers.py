# def check_even(number):
#     if number % 2 == 0
#         return True
#     return False
#
# result = filter(check_even, list(map(int, input().split(" "))))
# print(result)


def check_even(a):
    if a % 2 == 0:
        return True
    return False


sequence = input().split(" ")
print(list(filter(check_even, list(map(int, sequence)))))

# sequence = input().split(" ")
# result = list(filter(lambda x: x % 2 == 0, list(map(int, sequence))))
# print(result)