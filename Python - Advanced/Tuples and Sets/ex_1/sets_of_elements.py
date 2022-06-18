n, m = [int(x) for x in input().split(" ")]
n_set = set()
m_set = set()
for _ in range(n):
    current_num = int(input())
    n_set.add(current_num)
for _ in range(m):
    current_num = int(input())
    m_set.add(current_num)

intersection = n_set.intersection(m_set)
for num in intersection:
    print(num)