def trappedwater(li):
    n = len(li)
    if n == 0:
        return 0
    arr_left = [0] * n
    arr_right = [0] * n
    arr_left[0] = li[0]
    for i in range(1, n):
        arr_left[i] = max(arr_left[i-1], li[i])
    arr_right[n-1] = li[n-1]
    for i in range(n-2, -1, -1):
        arr_right[i] = max(arr_right[i+1], li[i])
    tw = 0
    for i in range(n):
        tw += min(arr_left[i], arr_right[i]) - li[i]  
    return tw
li = list(map(int, input().split()))
print(trappedwater(li))
