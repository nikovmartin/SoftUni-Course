first_seq = input().split(", ")
second_seq = input()
good_list = [word for word in first_seq if word in second_seq]
print(good_list)
