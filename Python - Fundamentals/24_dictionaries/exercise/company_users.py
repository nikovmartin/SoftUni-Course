company_members = {}
command = input().split(" -> ")
while command[0] != "End":
    company = command[0]
    id = command[1]
    if company not in company_members:
        company_members[company] = []
    if id not in company_members[company]:
        company_members[company].append(id)
    command = input().split(" -> ")
for company in company_members:
    print(f"{company}")
    for i in company_members[company]:
        print(f"-- {i}")