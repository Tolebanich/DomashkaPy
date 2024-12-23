from address import Address
from mailing import Mailing

to_address = Address(83000, "Магадан", "Ленина", 6, 34)
from_address = Address(83000, "Новосибирск", "Сталина", 1, 2)
mailing = Mailing(to_address, from_address, 5000, 123456789)

print(mailing)