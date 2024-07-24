n = input()
x = int(input())
for i in range(len(n) - 1, -1, -1):
    print(n[i], end = "")
    x -= 1
    if x == 0:
        break