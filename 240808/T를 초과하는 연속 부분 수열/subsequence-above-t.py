n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
arr_cnt = []
for i in range(len(arr)):
    if arr[i] > t:
        cnt += 1
    else:
        if cnt == 0:
            pass
        else:
            arr_cnt.append(cnt)
            cnt = 0
arr_cnt.sort(reverse = True)
print(arr_cnt[0])