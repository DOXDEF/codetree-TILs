arr_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
n = input()  # 이 변수는 사용되지 않습니다
arr_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        num = arr_1[i][j] * arr_2[i][j]
        print(num, end = " ")
    print()