n = input()
cnt_1 = 0
cnt_2 = 0
for i in range(len(n) - 1):
    if n[i] + n[i + 1] == 'ee':
        cnt_1 += 1
    elif n[i] + n[i + 1] == 'eb':
        cnt_2 += 1
print(cnt_1, cnt_2)