from student import Student
from course_group import CourseGroup


student = Student("Антон", "Оленёнок", 36, "QA")
classmate1 = Student("Мария", "Малахова", 31, "QA")
classmate2 = Student("Маргарита", "Мерлан", 30, "QA")
classmate3 = Student("Владислав", "Ребриков", 32, "QA")


course_group = CourseGroup(student,[classmate1, classmate2, classmate3])
print(course_group)