def is_vip(guest):
    return guest[0].isdigit()


n = int(input())
vip_list = set()
peasant_list = set()
for _ in range(n):
    reservation_num = input()
    if is_vip(reservation_num):
        vip_list.add(reservation_num)
    else:
        peasant_list.add(reservation_num)
while True:
    arrival = input()
    if arrival == "END":
        break
    if is_vip(arrival):
        vip_list.remove(arrival)
    else:
        peasant_list.remove(arrival)
print(len(vip_list) + len(peasant_list))
[print(guest) for guest in sorted(vip_list)]
[print(guest) for guest in sorted(peasant_list)]