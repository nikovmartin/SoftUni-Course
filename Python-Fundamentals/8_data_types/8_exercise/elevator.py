num_persons = int(input())
cap_persons = int(input())
courses = int(num_persons / cap_persons)
if num_persons % cap_persons == 0:
    print(courses)
else:
    print(courses + 1)