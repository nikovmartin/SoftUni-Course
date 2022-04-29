n = int(input())
for num in range (1,n+1):
    current_number = num
    sum_numbers = 0
    while current_number > 0:
        sum_numbers += current_number % 10
        current_number = current_number // 10
    if sum_numbers == 5 or sum_numbers == 7 or sum_numbers == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")