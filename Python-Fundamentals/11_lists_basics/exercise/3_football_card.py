# A = 11
# B = 11
# red_cards = input().split(" ")
# set_red_cards = set(red_cards)
# for team in set_red_cards:
#     if team[0] == "A":
#         A -= 1
#         if A < 7:
#             print(f"Team A - {A}; Team B - {B}")
#             print("Game was terminated")
#             break
#     else:
#         B -= 1
#         if A < 7:
#             print(f"Team A - {A}; Team B - {B}")
#             print("Game was terminated")
#             break
# if A > 6 and B > 6:
#     print(f"Team A - {A}; Team B - {B}")

A = 11
B = 11
red_cards = input().split(" ")
players_out = list()
game_stopped = False
for player in red_cards:
    if player not in players_out:
        players_out.append(player)
        if "A" in player:
            A -= 1
        else:
            B -= 1
        if A < 7 or B < 7:
            game_stopped = True
            break
print(f"Team A - {A}; Team B - {B}")
if game_stopped is True:
    print("Game was terminated")