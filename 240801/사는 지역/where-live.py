class Human:
    def __init__(self, name, number, country):
        self.name = name
        self.number = number
        self.country = country

humans = []
answer = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    humans.append(Human(a, b, c))
sorted_humans = sorted(humans, key=lambda x: x.name)
answer = sorted_humans[n - 1]
print("name " + answer.name)
print("addr " + answer.number)
print("city " + answer.country)