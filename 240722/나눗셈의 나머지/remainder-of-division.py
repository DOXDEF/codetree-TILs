a, b = map(int, input().split())
count_arr = [0 for _ in range(b)]
sum_cnt = 0
while True:
    count_arr[a % b] += 1
    if a // b <= 1:
        break
    a //= b
for i in count_arr:
    sum_cnt += i * i
print(sum_cnt)