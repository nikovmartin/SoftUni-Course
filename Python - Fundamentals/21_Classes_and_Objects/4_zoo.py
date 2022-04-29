class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammal.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.bird.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammal)}" \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fish)}" \
                   f"\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.bird)}" \
                   f"\nTotal animals: {Zoo.__animals}"


name_of_zoo = input()
zoo = Zoo(name_of_zoo)

for i in range (int(input())):
    explode = input().split(" ")
    species = explode[0]
    type_of_animal = explode[1]
    zoo.add_animals(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))

