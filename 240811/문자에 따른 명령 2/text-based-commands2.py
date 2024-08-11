dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
n = input()
idx = 100000
for i in range(len(n)):
    if n[i] == 'L':
        idx -= 1
    elif n[i] == 'R':
        idx += 1
    else:
        x, y = x + dx[idx % 4], y + dy[idx % 4]
print(x, y)