import re
text = input()
total_pattern = r"(^|(?<=\s))[a-zA-Z0-9]([a-zA-Z0-9\.\-\_]*[a-zA-Z0-9])*[@][a-zA-Z]([a-zA-Z0-9\-]*[a-zA-Z])*(\.[a-zA-Z]([a-zA-Z\-]*[a-zA-Z])*)+"
emails = re.finditer(total_pattern, text)
for email in emails:
    print(email.group())
