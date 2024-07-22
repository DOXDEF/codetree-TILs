a, b = map(int, input().split())
count_arr = [0 for _ in range(b)]
while True:
    count_arr[a % b] += 1