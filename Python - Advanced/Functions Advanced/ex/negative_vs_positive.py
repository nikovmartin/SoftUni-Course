numbers = [int(x) for x in input().split(" ")]
positive = []
negative = []
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
print(sum(negative))
print(sum(positive))
if sum(positive) > abs(sum(negative)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")