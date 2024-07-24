n = 10
arr = [
    input()
    for _ in range(n)
]
x = input()
cnt = 0
for i in arr:
    if i[len(i) - 1] == x:
        print(i)
        cnt += 1
if cnt == 0:
    print("None")