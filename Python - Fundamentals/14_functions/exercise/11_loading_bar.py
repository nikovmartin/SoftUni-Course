# def loading_bar(num):
#     percentages_list = list()
#     for i in range(1, 11):
#         if i <= num // 10:
#             percentages_list.append("%")
#         else:
#             percentages_list.append(".")
#     if num == 100:
#         print("100% Complete!")
#         print("[%%%%%%%%%%]")
#     else:
#         print(f'{num}% [{"".join(percentages_list)}]')
#         print("Still loading...")
#
#
# number = int(input())
# loading_bar(number)



def loading_bar(num):
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f'{num}% [{(num // 10) * "%"}{(10 - (num // 10)) * "." }]')
        print("Still loading...")


number = int(input())
loading_bar(number)