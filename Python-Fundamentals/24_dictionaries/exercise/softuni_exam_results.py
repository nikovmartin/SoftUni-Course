username_dict = {}
language_dict = {}

line = input().split("-")
while line[0] != "exam finished":
    name = line[0]
    language = line[1]
    if language == "banned":
        del username_dict[name]
        break
    score = line[2]
    if name not in username_dict:
        username_dict[name] = score
    elif name in username_dict:
        if username_dict[name] < score:
            username_dict[name] = score
    if language not in language_dict:
        language_dict[language] = 1
    else:
        language_dict[language] += 1
    line = input().split("-")
print("Results:")
for user in username_dict:
    print(f"{user} | {username_dict[user]}")
print("Submissions:")
for language in language_dict:
    print(f"{language} - {language_dict[language]}")