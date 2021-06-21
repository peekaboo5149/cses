try:
    n = int(input())
    arr = list(map(lambda val: int(val), input().split(" ")))
    # CODE
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            diff = arr[i] - arr[i + 1]
            arr[i + 1] = arr[i]
            count += diff
    print(count)
except Exception:
    pass
