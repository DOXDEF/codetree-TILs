class Dot:
    def __init__(self, x, y, dist, number):
        self.x = x
        self.y = y
        self.dist = dist
        self.number = number

n = int(input())
dots = []
for i in range(n):
    a, b = map(int, input().split())
    dots.append(Dot(a, b, abs(a) + abs(b), i + 1))

sorted_dots = sorted(dots, key = lambda x: (x.dist, x.number))
for i in range(n):
    print(sorted_dots[i].number)