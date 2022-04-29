def perfect_number(a):
    sum = 0
    for i in range(1, a):
        if a % i == 0:
            sum += i
    if sum == a:
        print(" We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
