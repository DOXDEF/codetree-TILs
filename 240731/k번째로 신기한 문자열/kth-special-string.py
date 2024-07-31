n, k, t = map(str, input().split())
n = int(n)
k = int(k)
arr = []
answer = []
for _ in range(n):
    arr.append(input())
for i in arr:
    if i[:len(t)] == t:
        answer.append(i)
answer.sort()
print(answer[k - 1])