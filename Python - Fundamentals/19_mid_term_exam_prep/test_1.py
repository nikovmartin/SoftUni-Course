array = [1, 2, 3, 4, 5]
array = list(map(str, array))
array[2], array[4] = array[4], array[2]
print(", ".join(array))