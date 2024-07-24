n = input()
a = n[0]
cnt = 0
x = ''
for i in range(len(n)):
    if n[i] == a:
        cnt += 1
    else:
        x += a + str(cnt)
        a = n[i]
        cnt = 1
x += a + str(cnt)
print(f"""{len(x)}
{x}""")