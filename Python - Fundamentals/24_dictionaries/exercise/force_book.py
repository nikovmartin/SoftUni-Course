sides_dict = {}
force_user_list = []
line = input()

while line != "Lumpawaroo":
    if "|" in line:
        explode = line.split(" | ")
        side = explode[0]
        force_user = explode[1]

        if side not in sides_dict and force_user not in force_user_list:
            sides_dict[side] = []
            sides_dict[side].append(force_user)
            force_user_list.append(force_user)
        elif side in sides_dict and force_user not in force_user_list:
            sides_dict[side].append(force_user)
            force_user_list.append(force_user)

    elif "->" in line:
        explode = line.split(" -> ")
        side = explode[1]
        force_user = explode[0]

        if side not in sides_dict and force_user not in force_user_list:
            sides_dict[side] = []
            sides_dict[side].append(force_user)
            force_user_list.append(force_user)
        elif side in sides_dict and force_user not in force_user_list:
            sides_dict[side].append(force_user)
            force_user_list.append(force_user)
        elif force_user in force_user_list:
            for current_side in sides_dict:
                if force_user in sides_dict[current_side]:
                    if len(sides_dict[current_side]) > 1:
                        sides_dict[current_side].remove(force_user)
                        break
                    else:
                        del sides_dict[current_side]
                        break
            sides_dict[side].append(force_user)

        print(f"{force_user} joins the {side} side!")

    line = input()

for side in sides_dict:
    print(f"Side: {side}, Members: {len(sides_dict[side])}")
    for user in sides_dict[side]:
        print(f"! {user}")