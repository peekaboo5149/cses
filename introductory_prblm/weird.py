try:
    n = int(input())
    ll = list()
    ll.append(n)
    count = True
    while count:
        if n % 2 == 0:
            n /= 2
            n = int(n)
            ll.append(n)
        elif n == 1:
            count = False
            break
        else:
            n = 3 * n + 1
            ll.append(n)

    for item in ll:
        print(item,end=" ")
except Exception:
    pass
