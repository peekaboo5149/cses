try:
    n = int(input())
    arr = list(map(lambda val: int(val), input().split(" ")))

    expected_sum = n * (n + 1) / 2
    got_sum = 0
    for a in arr:
        got_sum += a
    print(int(expected_sum - got_sum))
except Exception:
    pass
