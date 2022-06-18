seq_one = set([int(x) for x in input().split(" ")])
seq_two = set([int(x) for x in input().split(" ")])
n = int(input())
for i in range(n):
    command = input().split(" ")
    if command[0] == "Check":
        condition = False
        if seq_one.issubset(seq_two):
            condition = True
        if seq_two.issubset(seq_one):
            condition = True
        print(condition)
    expression = set(int(x) for x in command[2:])
    if command[0] == "Add":
        if command[1] == "First":
            seq_one = seq_one.union(expression)
        else:
            seq_two = seq_two.union(expression)
    elif command[0] == "Remove":
        if command[1] == "First":
            seq_one = seq_one.difference(expression)
        else:
            seq_two = seq_two.difference(expression)
print(*sorted(seq_one), sep=", ")
print(*sorted(seq_two), sep=", ")