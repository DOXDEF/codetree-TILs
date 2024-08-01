class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

humans = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    humans.append(Human(a, b, c))
sorted_humans = sorted(humans, key=lambda x: x.height)
for i in range(n):
    print(sorted_humans[i].name, sorted_humans[i].height, sorted_humans[i].weight)