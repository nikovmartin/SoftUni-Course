electrons = int(input())
shells = []
num = 1
while electrons - 2 * num * num > 0:
    shells.append(2 * num * num)
    electrons = electrons - 2 * num * num
    num += 1
if electrons > 0:
    shells.append(electrons)
print(shells)