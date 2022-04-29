# sequence = input().split(" ")
# result = sorted(list(map(int, sequence)))
# print(f"The minimum number is {result[0]}")
# print(f"The maximum number is {result[-1]}")
# print(f"The sum number is: {sum(result)}")

# sequence = input().split(" ")
# result = sorted(list(map(int, sequence)))
# print(f"The minimum number is {min(result)}")
# print(f"The maximum number is {max(result)}")
# print(f"The sum number is: {sum(result)}")


def min_max_sum(final_result):
    print(f"The minimum number is {min(final_result)}")
    print(f"The maximum number is {max(final_result)}")
    print(f"The sum number is: {sum(final_result)}")


sequence = input().split(" ")
result = sorted(list(map(int, sequence)))
min_max_sum(result)

