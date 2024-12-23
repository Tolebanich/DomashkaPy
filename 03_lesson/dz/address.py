class Address:
    def __init__(self, index, city, street, dom, num_kv):
        self.index = index
        self.city = city
        self.street = street
        self.dom = dom
        self.num_kv = num_kv

    def __str__(self):
        return (f"{self.index}, {self.city}, {self.street}, {self.dom}-{self.num_kv}")