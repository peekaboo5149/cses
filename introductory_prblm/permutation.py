try:
    n = int(input())
    if n == 1:
        print('1')
        exit()
    elif n <= 3:
        print('NO SOLUTION')
    elif n == 4:
        print('3 1 4 2')
    else:
        even_n = int(n >> 1)  # 2
        # print(even_n)
        for i in range(1, even_n+1):
            print((i << 1), end=" ")
        for i in range(1, n-even_n+1):
            print((i << 1)-1, end=" ")

except Exception:
    pass
