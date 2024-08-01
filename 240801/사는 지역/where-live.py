class Human:
    def __init__(self, name, number, country):
        self.name = name
        self.number = number
        self.country = country

humans = []
n = int(input())
for _ in range(n):
    name, number, country = tuple(map(str, input().split()))
    humans.append(Human(name, number, country))
sorted(humans, key=lambda x: x.name)
answer = humans[n - 1]
print("name " + answer.name)
print("addr " + answer.number)
print("city " + answer.country)