class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
students = []
for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i + 1))
sorted_students = sorted(students, key=lambda x: (x.height, x.weight), reverse = True)
for i in range(n):
    print(sorted_students[i].height, sorted_students[i].weight, sorted_students[i].number)