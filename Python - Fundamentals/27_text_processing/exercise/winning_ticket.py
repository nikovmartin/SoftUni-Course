def winning_ticket(symbol):
    counter_left = 0
    counter_right = 0
    for i in range(len(left)):
        if left[i] == symbol:
            counter_left += 1
        elif left[i] != symbol and counter_left >= 6:
            break
        else:
            counter_left = 0
    for i in range(len(right)):
        if right[i] == symbol:
            counter_right += 1
        elif right[i] != symbol and counter_right >= 6:
            break
        else:
            counter_right = 0
    counter = min(counter_left, counter_right)
    print(f'ticket "{ticket}" - {counter}{symbol}')


tickets_info = input()
tickets = [x.strip() for x in tickets_info.split(",")]
for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    elif ticket[0] * 20 == ticket and ticket[0] in "@$#^":
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    else:
        half = int((len(ticket)) / 2)
        left = ticket[0:half]
        right = ticket[half:]
        if (6 * '@') in left and (6 * '@') in right:
            winning_ticket("@")
        elif (6 * '$') in left and (6 * '$') in right:
            winning_ticket("$")
        elif (6 * '#') in left and (6 * '#') in right:
            winning_ticket("#")
        elif (6 * '^') in left and (6 * '^') in right:
            winning_ticket("^")
        else:
            print(f'ticket "{ticket}" - no match')