n = int(input())
arr = list(map(float, input().split()))
eva = sum(arr) / n
print(f"{eva:.1f}")
if eva >= 4.0:
    print("Perfect")
elif eva >= 3.0:
    print("Good")
else:
    print("Poor")