arr = list(map(int, input().split()))
print(f"{sum(arr[1::2])} {sum(arr[2::3]) / len(arr[2::3]):.1f}")