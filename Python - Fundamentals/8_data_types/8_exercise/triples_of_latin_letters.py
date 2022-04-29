num = int(input())
for q in range (0,num):
    for w in range (0,num):
        for e in range (0,num):
            print(f"{chr(q + 97)}{chr(w + 97)}{chr(e + 97)}")