n = int(input())
odd_set = set()
even_set = set()
for i in range(1, n + 1):
    name = input()
    calculation = sum([ord(x) for x in name]) // i
    if calculation % 2 == 0:
        even_set.add(calculation)
    else:
        odd_set.add(calculation)

sum_odd_set = sum(odd_set)
sum_even_set = sum(even_set)
if sum_odd_set == sum_even_set:
    print(", ".join([str(x) for x in odd_set.union(even_set)]))
elif sum_odd_set > sum_even_set:
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))