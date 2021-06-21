try:
    s = input()
    count = 0
    mmax = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            if mmax < count:
                mmax = count
        else:
            count = 0
    print(mmax+1)
except Exception:
    pass
