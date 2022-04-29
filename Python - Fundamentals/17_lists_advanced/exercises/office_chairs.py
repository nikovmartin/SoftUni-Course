rooms = int(input())
extra_chairs = 0
problems = False

for i in range(rooms):
    data = input().split(" ")
    chairs = data[0]
    visitors = int(data[1])
    if len(chairs) < visitors:
        diff = visitors - len(chairs)
        print(f"{diff} more chairs needed in room {i + 1}")
        problems = True
    elif len(chairs) >= visitors:
        extra_chairs += (len(chairs) - visitors)

if problems is False:
    print(f"Game On, {extra_chairs} free chairs left")