from user import User
from card import Card

Alex = User("Alex")
Mark = User("Mark")
Marta = User("Marta")

card = Card("1234 5678 9123 4567", "11/28", "Alex F")

Alex.sayName()
Alex.setAge(33)
Alex.sayAge()
Alex.addCard(card)
Alex.getCard().pay(1000)
