arr = []
sum = 0
count = 0
for _ in range(10):
    arr.append(int(input()))
for i in arr:
    if i >= 0 and i <= 200:
        sum += i
        count += 1
print(f"{sum} {sum / count:.1f}")