# import re
# text = input()
# travel_points = 0
# rule = r"(?<=\=)[A-Z][a-zA-Z][a-zA-Z]+(?=\=)|(?<=\/)[A-Z][a-zA-Z][a-zA-Z]+(?=\/)"
# result = re.findall(rule, text)
# for dest in result:
#     travel_points += len(dest)
# result = ", ".join(result)
# print(f"Destinations: {result}")
# print(f"Travel Points: {travel_points}")



import re
text = input()
travel_points = 0
locations = list()
rule = r"([=/])([A-Z][a-zA-Z]{2,})\1"
result = re.finditer(rule, text)
for dest in result:
    locations.append(dest[2])
    travel_points += len(dest[2])
result = ", ".join(locations)
print(f"Destinations: {result}")
print(f"Travel Points: {travel_points}")





