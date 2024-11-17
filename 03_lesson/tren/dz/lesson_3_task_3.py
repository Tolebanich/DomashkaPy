from adress import Adress
from mailing import Mailing

to_adress = Adress(83000, "Магадан", "Ленина", 6, 34)
from_adress = Adress(83000, "Новосибирск", "Сталина", 1, 2)
mailing = Mailing(to_adress, from_adress, 5000, 123456789)

print(mailing)