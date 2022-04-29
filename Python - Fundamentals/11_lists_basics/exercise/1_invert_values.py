number = input().split(" ")
reverted_list = list()
for current_num in number:
    if int(current_num) > 0:
        reverted_list.append(-int(current_num))
    else:
        reverted_list.append(abs(int(current_num)))
print(reverted_list)