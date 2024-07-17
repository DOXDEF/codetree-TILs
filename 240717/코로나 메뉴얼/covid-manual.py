count = 0
for i in range(3):
    a, b = None, None
    a, b = map(str, input().split())
    if a == 'Y':
        if int(b) >= 37:
            count += 1
if count >= 2:
    print('E')
else:
    print('N')