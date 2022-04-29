# text = input().split(" ")
# result = 0
# a = text[0]
# b = text[1]
#
# if len(a) == len(b):
#     for i in range(len(a)):
#         result += ord(a[i]) * ord(b[i])
# elif len(a) > len(b):
#     diff = len(a) - len(b)
#     for i in range(diff):
#         b += chr(1)
#     for i in range(len(a)):
#         result += ord(a[i]) * ord(b[i])
# else:
#     diff = len(b) - len(a)
#     for i in range(diff):
#         a += chr(1)
#     for i in range(len(b)):
#         result += ord(a[i]) * ord(b[i])
#
# print(result)

# text = input().split(" ")
# result = 0
# a = text[0]
# b = text[1]
# diff = abs(len(a) - len(b))
#
# for i in range(min(len(a), len(b))):
#     result += ord(a[i]) * ord(b[i])
# if len(a) > len(b):
#     for i in a[-diff:]:
#         result += ord(i)
# elif len(b) > len(a):
#     for i in b[-diff:]:
#         result += ord(i)
#
# print(result)

text = input().split(" ")
result = 0
a = text[0]
b = text[1]

for i in range(max(len(a), len(b))):
    if len(a) > len(b):
        if len(b) > i:
            result += ord(a[i]) * ord(b[i])
        else:
            result += ord(a[i])
    elif len(b) > len(a):
        if len(a) > i:
            result += ord(a[i]) * ord(b[i])
        else:
            result += ord(b[i])
    else:
        result += ord(a[i]) * ord(b[i])
print(result)