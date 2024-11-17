class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def prodNP(self):
        return f"Name_prod: {self.name}, Price:{self.price}"