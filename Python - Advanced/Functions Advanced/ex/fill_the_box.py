# def fill_the_box(*args):
#     box_size = args[0] * args[1] * args[2]
#     cubes = args[3:]
#     sum_cubes = 0
#
#     for cube in cubes:
#         if cube == "Finish":
#             break
#         else:
#             sum_cubes += cube
#
#     residual_cubes = box_size - sum_cubes
#
#     if residual_cubes > 0:
#         return f"There is free space in the box. You could put {residual_cubes} more cubes."
#     else:
#         for cube in cubes:
#             if box_size >= cube:
#                 box_size -= cube
#                 sum_cubes -= cube
#             else:
#                 sum_cubes -= box_size
#                 return f"No more free space! You have {sum_cubes} more cubes."
#
#
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))




def fill_the_box(h, l, w, *args):
    box_size = h * l * w
    left_cubes = 0

    for el in args:
        if el == "Finish":
            break
        if box_size >= el:
            box_size -= el
        else:
            el -= box_size
            box_size = 0
            left_cubes += el

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    else:
        return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))




