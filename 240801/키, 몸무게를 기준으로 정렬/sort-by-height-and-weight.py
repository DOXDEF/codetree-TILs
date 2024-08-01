class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
students = []
for i in range(n):
    a, b, c = map(str, input().split())
    students.append(Student(a, int(b), float(c)))

sorted_students = sorted(students, key = lambda x: (x.height, -x.weight))
for i in range(n):
    print(f"{sorted_students[i].name} {sorted_students[i].height} {sorted_students[i].weight:.0f}")