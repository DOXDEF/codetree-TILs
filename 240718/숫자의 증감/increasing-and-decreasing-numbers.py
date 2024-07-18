c, n = map(str, input().split())
count_a = 1
count_d = int(n)
if c == 'A':
    while count_a <= count_d:
        print(count_a, end = " ")
        count_a += 1
else:
    while count_d >= count_a:
        print(count_d, end = " ")
        count_d -= 1