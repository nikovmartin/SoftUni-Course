# def even_odd(type, num_list):
#     parity = 0 if type == "even" else 1
#     return [x for x in num_list if x % 2 == parity]
#
#
# def even_odd_filter(**kwargs):
#     final_dict = {
#     }
#     for type, num_list in kwargs.items():
#         if type not in final_dict:
#             final_dict[type] = []
#         final_dict[type].extend(even_odd(type, num_list))
#
#     return final_dict
#
#
#

def even_odd_filter(**kwargs):
    final_dict = {
    }
    for type, num_list in kwargs.items():
        parity = 0 if type == "even" else 1
        if type not in final_dict:
            final_dict[type] = []
        final_dict[type].extend([x for x in num_list if x % 2 == parity])

    # return dict(sorted(final_dict.items(), key= lambda x: len(x[1]), reverse=True))
    return {key: value for key, value in sorted(final_dict.items(), key= lambda x: -len(x[1]))}



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

