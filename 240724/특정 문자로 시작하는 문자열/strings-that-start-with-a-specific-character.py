n = int(input())
arr = [
    input()
    for _ in range(n)
]
x = input()
cnt = 0
avg = 0
for i in arr:
    if i[0] == x:
        cnt += 1
        avg += len(i)
print(f"{cnt} {avg / cnt:.2f}")