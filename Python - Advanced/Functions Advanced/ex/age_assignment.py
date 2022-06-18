def age_assignment(*args, **kwargs):
    age_dict = {}
    for name in args:
        age_dict[name] = kwargs[name[0]]
    sorted_names = sorted(age_dict.items(), key=lambda x: x[0])
    text = [f"{key} is {value} years old." for key, value in sorted_names]
    return "\n".join(text)

print(age_assignment("Peter", "George", G=26, P=19))