x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())
cnt = 0
answer = -1
for i in range(n):
    d, t = map(str, input().split())
    if d == 'E':
        dir_num = 0
        for j in range(int(t)):
            x, y = x + dx[dir_num], y + dy[dir_num]
            cnt += 1
            if x == 0 and y == 0:
                answer = cnt
                break
    elif d == 'S':
        dir_num = 1
        for j in range(int(t)):
            x, y = x + dx[dir_num], y + dy[dir_num]
            cnt += 1
            if x == 0 and y == 0:
                answer = cnt
                break
    elif d == 'W':
        dir_num = 2
        for j in range(int(t)):
            x, y = x + dx[dir_num], y + dy[dir_num]
            cnt += 1
            if x == 0 and y == 0:
                answer = cnt
                break
    elif d == 'N':
        dir_num = 3
        for j in range(int(t)):
            x, y = x + dx[dir_num], y + dy[dir_num]
            cnt += 1
            if x == 0 and y == 0:
                answer = cnt
                break
print(answer)