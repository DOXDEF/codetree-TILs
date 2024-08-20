n = input()
idx = ''
cnt = 0
for i in range(len(n) - 1):
    if n[i] == '(' and n[i + 1] == '(':
        for j in range(i + 2, len(n) - 1):
            if n[j] == ')' and n[j + 1] == ')':
                cnt += 1
print(cnt)