class Student:
    def __init__(self, name, fname, age, course):
        self.name = name
        self.fname = fname
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.name} {self.fname}, {self.age} лет, {self.course} курс"