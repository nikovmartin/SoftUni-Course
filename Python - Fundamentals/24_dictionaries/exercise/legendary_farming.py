# legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
# junk_items_dict = {}
# condition = False
# while condition is False:
#     finds = list(map(lambda x: x.lower(), input().split(" ")))
#     for i in range(1, len(finds), 2):
#         material = finds[i]
#         qty = int(finds[i-1])
#         if material in legendary_items_dict:
#             legendary_items_dict[material] += qty
#         elif material not in junk_items_dict:
#             junk_items_dict[material] = qty
#         else:
#             junk_items_dict[material] += qty
#         for item in legendary_items_dict:
#             if legendary_items_dict[item] >= 250:
#                 if item == "shards":
#                     print(f"Shadowmourne obtained!")
#                 elif item == "fragments":
#                     print(f"Valanyr obtained!")
#                 elif item == "motes":
#                     print(f"Dragonwrath obtained!")
#                 legendary_items_dict[item] -= 250
#                 condition = True
#         if condition is True:
#             break
# for item, value in legendary_items_dict.items():
#     print(f"{item}: {value}")
# for item, value in junk_items_dict.items():
#     print(f"{item}: {value}")


legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_items_dict = {}
condition = False
while condition is False:
    finds = list(map(lambda x: x.lower(), input().split(" ")))
    for i in range(1, len(finds), 2):
        material = finds[i]
        qty = int(finds[i-1])
        if material in legendary_items_dict:
            legendary_items_dict[material] += qty
            if legendary_items_dict[material] >= 250:
                if material == "shards":
                    print(f"Shadowmourne obtained!")
                elif material == "fragments":
                    print(f"Valanyr obtained!")
                elif material == "motes":
                    print(f"Dragonwrath obtained!")
                legendary_items_dict[material] -= 250
                condition = True
        elif material not in junk_items_dict:
            junk_items_dict[material] = qty
        else:
            junk_items_dict[material] += qty
        if condition is True:
            break
for item, value in legendary_items_dict.items():
    print(f"{item}: {value}")
for item, value in junk_items_dict.items():
    print(f"{item}: {value}")