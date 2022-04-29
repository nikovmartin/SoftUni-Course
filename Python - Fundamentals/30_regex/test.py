import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print(f"The first whitespace: {x.start()}")