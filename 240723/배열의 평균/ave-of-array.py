arr_2d = []
val_all = 0
for i in range(2):
    arr = list(map(int, input().split()))
    arr_2d.append(arr)
for i in range(2):
    val_x = 0
    for j in range(4):
        val_x += arr_2d[i][j]
    print(f"{val_x / 4:.1f}", end = " ")
print()
for i in range(4):
    val_y = 0
    for j in range(2):
        val_y += arr_2d[j][i]
    print(f"{val_y / 2:.1f}", end = " ")
print()
for i in range(2):
    for j in range(4):
        val_all += arr_2d[i][j]
print(f"{val_all / 8:.1f}", end = " ")