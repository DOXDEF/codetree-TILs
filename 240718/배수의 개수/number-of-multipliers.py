arr = []
for _ in range(10):
    arr.append(int(input()))
cnt_3 = 0
cnt_5 = 0
for i in arr:
    if i % 3 == 0:
        cnt_3 += 1
    if i % 5 == 0:
        cnt_5 += 1
print(cnt_3, cnt_5)