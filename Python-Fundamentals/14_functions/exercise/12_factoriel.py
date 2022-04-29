# РЕКУРСИЯ
def factoriel_calc(x):
    # sum = 1
    # for i in range(1, x + 1):
    #     sum = i * sum
    # return sum
    return 1 if x == 0 or x == 1 else x * factoriel_calc(x - 1)


num_1 = int(input())
num_2 = int(input())

result = factoriel_calc(num_1) / factoriel_calc(num_2)

print(f"{result:.2f}")