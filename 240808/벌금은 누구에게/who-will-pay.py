n, m, k = map(int, input().split())
arr_stu = [0 for _ in range(n)]
answer = -1
for _ in range(m):
    x = int(input())
    arr_stu[x - 1] += 1
    if arr_stu[x - 1] == k:
        answer = x
        break
print(answer)