class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if x[0] == first_letter]

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        output += "\n".join(sorted(self.products))
        return output


