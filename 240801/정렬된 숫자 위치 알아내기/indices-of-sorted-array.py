class Direction:
    def __init__(self, number, first_idx, second_idx):
        self.number = number
        self.first_idx = first_idx
        self.second_idx = second_idx

n = int(input())
arr = list(map(int, input().split()))
directions = []
for i in range(n):
    directions.append(Direction(arr[i], i + 1, 0))
directions = sorted(directions, key = lambda x: (x.number, x.first_idx))
for i in range(n):
    directions[i].second_idx = i + 1
directions = sorted(directions, key = lambda x: x.first_idx)
for i in range(n):
    print(directions[i].second_idx, end = " ")