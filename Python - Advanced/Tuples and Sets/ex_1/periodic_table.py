# n = int(input())
# unique_el = set()
# for _ in range(n):
#     curr_line = input().split(" ")
#     for el in curr_line:
#         unique_el.add(el)
# for el in unique_el:
#     print(el)

n = int(input())
unique_el = set()
for _ in range(n):
    curr_line = set(input().split(" "))
    unique_el = unique_el.union(curr_line)
for el in unique_el:
    print(el)