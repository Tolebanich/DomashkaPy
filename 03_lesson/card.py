class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknown'

    def __init__(self, number, validDate, holder):
        self.holder = holder
        self.number = number
        self.validDate = validDate

    def pay(self, amount):
        print("с карты ", self.number, "списали", amount)