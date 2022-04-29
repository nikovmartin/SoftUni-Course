# num_list = []
# for i in range(5):
#     num_list.append(i)
#
# print(num_list)
# # =
# num_list_2 = [i for i in range(5)]
#


# list = [1, 2, 3, 1, 2, 1]
# for i in list:
#     if i == 1:
#         list.remove(i)
# print(list)
#
# list_without_one = [list.remove(i) for i in list if i == 1]
# print(list)



number_list = [1, 2, 3, 4]
double_list = [i * 2 for i in number_list]
double_list_2 = list(map(lambda x: x*2, number_list))
print(double_list)
print(double_list_2)

