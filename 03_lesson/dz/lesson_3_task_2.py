from smartphone import Smartphone

catalog = [
    Smartphone("redmi 12","xiaomi","+79494677244"),
    Smartphone("redmi 11", "xiaomi", "+9981124578"),
    Smartphone("redmi 13", "xiaomi", "+9986665577"),
    Smartphone("redmi 14", "xiaomi", "+9983035033"),
    Smartphone("iphone 14", "apple", "+79994445566")
]

for smartphone in catalog:
    print(f"{smartphone.mark},{smartphone.model},{smartphone.number}")