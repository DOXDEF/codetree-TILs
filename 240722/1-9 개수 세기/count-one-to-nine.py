n = int(input())
count_arr = [0 for i in range(10)]
arr = list(map(int, input().split()))
for i in arr:
    count_arr[i] += 1
for i in range(1,10):
    print(count_arr[i])