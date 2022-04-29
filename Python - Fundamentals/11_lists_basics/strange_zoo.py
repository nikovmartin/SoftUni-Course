# tail = input()
# body = input()
# head = input()
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[-1], meerkat[-3]
# print(meerkat)

tail = input()
body = input()
head = input()
meerkat = [tail, body, head]
switch = meerkat [0]
meerkat[0] = meerkat[2]
meerkat[2] = switch
print(meerkat)