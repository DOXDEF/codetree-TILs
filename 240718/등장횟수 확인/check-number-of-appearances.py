arr = []
cnt = 0
for _ in range(5):
    arr.append(int(input()))
for i in arr:
    if i % 2 == 0:
        cnt += 1
print(cnt)