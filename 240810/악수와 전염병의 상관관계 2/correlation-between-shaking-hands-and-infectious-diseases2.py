n, k, p, t = map(int, input().split())
timeline = []
arr_virus = [k for _ in range(n)]
arr_infect = [0 for _ in range(n)]
arr_infect[p - 1] = 1
for _ in range(t):
    a, b, c = map(int, input().split())
    timeline.append([a, b, c])
timeline.sort()
for i in range(len(timeline)):
    if (arr_infect[timeline[i][1] - 1] == 1 and arr_infect[timeline[i][2] - 1] == 0 and arr_virus[timeline[i][1] - 1] != 0):
        arr_infect[timeline[i][2] - 1] = 1
        arr_virus[timeline[i][1] - 1] -= 1
    elif (arr_infect[timeline[i][2] - 1] == 1 and arr_infect[timeline[i][1] - 1] == 0 and arr_virus[timeline[i][2] - 1] != 0):
        arr_infect[timeline[i][1] - 1] = 1
        arr_virus[timeline[i][2] - 1] -= 1
    elif ((arr_infect[timeline[i][2] - 1] == 1 and arr_infect[timeline[i][1] - 1] == 1 
        and arr_virus[timeline[i][2] - 1] != 0 and arr_virus[timeline[i][1] - 1] != 0)):
        if arr_virus[timeline[i][1] - 1] != 0:
            arr_virus[timeline[i][1] - 1] -= 1
        if arr_virus[timeline[i][2] - 1] != 0:
            arr_virus[timeline[i][2] - 1] -= 1
for i in arr_infect:
    print(i, end = "")