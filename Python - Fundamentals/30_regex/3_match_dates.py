import re
text = input()
expression = r"\b(?P<day>\d{2})([/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
matches = re.finditer(expression, text)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")