# def math_operations(*args,**kwargs):
#     counter = 0
#     final_list = []
#     for idx in range(len(args)):
#         if counter == 4:
#             counter = 0
#         counter += 1
#         if counter == 1:
#             kwargs["a"] += args[idx]
#         elif counter == 2:
#             kwargs["s"] -= args[idx]
#         elif counter == 3:
#             if args[idx] == 0:
#                 continue
#             kwargs["d"] = kwargs["d"] / args[idx]
#         elif counter == 4:
#             kwargs["m"] *= args[idx]
#     sorted_kwargs = dict(sorted(kwargs.items(), key= lambda x: (-x[1],x[0])))
#     for key, value in sorted_kwargs.items():
#         final_list.append(f"{key}: {value:.1f}")
#     return "\n".join(final_list)

def math_operations(*args,**kwargs):
    counter = 0
    final_list = []
    for idx in range(len(args)):
        if counter == 4:
            counter = 0
        counter += 1
        if counter == 1:
            kwargs["a"] += args[idx]
        elif counter == 2:
            kwargs["s"] -= args[idx]
        elif counter == 3:
            if args[idx] == 0:
                continue
            kwargs["d"] = kwargs["d"] / args[idx]
        elif counter == 4:
            kwargs["m"] *= args[idx]
    sorted_kwargs = sorted(kwargs.items(), key= lambda x: (-x[1],x[0]))
    for el in sorted_kwargs:
        final_list.append(f"{el[0]}: {el[1]:.1f}")
    return "\n".join(final_list)


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))