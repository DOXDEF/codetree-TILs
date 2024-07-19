n = int(input())
arr = []
sum = 0
for _ in range(n):
    arr.append(int(input()))
for i in arr:
    sum += i
print(f"{sum} {sum / n:.1f}")