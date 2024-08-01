class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []
for i in range(5):
    a, b, c = map(str, input().split())
    students.append(Student(a, b, c))

sorted_students1 = sorted(students, key = lambda x: x.name)
print("name")
for i in range(5):
    print(sorted_students1[i].name, sorted_students1[i].height, sorted_students1[i].weight)
    
sorted_students2 = sorted(students, key = lambda x: x.height, reverse = True)
print("""
height""")
for i in range(5):
    print(sorted_students2[i].name, sorted_students2[i].height, sorted_students2[i].weight)