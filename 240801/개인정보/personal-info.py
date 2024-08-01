class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []
for i in range(5):
    a, b, c = map(str, input().split())
    students.append(Student(a, b, c))
sorted_students = sorted(students, key = lambda x: x.)