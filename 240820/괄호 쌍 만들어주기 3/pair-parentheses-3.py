n = input()
idx = ''
cnt = 0
for i in range(len(n)):
    idx = n[i]
    if idx == '(':
        for j in range(i + 1, len(n)):
            if n[j] == ')':
                cnt += 1
print(cnt)