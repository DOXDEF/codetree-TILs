class Human:
    def __init__(self, name, number, country):
        self.name = name
        self.number = number
        self.country = country
    def __repr__(self):
        return repr((self.name, self.number, self.country))

humans = []
n = int(input())
for _ in range(n):
    a, b, c = input().split()
    humans.append(Human(a, b, c))
sorted(humans, key=lambda x: x.name)
answer = humans[n - 1]
print("name " + answer.name)
print("addr " + answer.number)
print("city " + answer.country)