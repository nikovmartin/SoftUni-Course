countries = input().split(", ")
capitals = input().split(", ")
capital_cities = dict(zip(countries, capitals))
for country, capital in capital_cities.items():
    print(f"{country} -> {capital}")