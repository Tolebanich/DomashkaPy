from math import ceil

def square(a):
    s = a * a
    return s

a = float(input("Длина: "))
result = square(a)
rounded = ceil(result)
print(f"Площадь квадр: {rounded}")