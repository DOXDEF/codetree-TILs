a = input()
b = input()
c = input()
arr = []
arr.append(abs(len(a) - len(b)))
arr.append(abs(len(b) - len(c)))
arr.append(abs(len(c) - len(a)))
arr = sorted(arr, reverse = True)
print(arr[0])