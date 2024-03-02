h, m = map(int, input().split())

if m != 45:
    if h > 0:
        print(h - 1, 60 - abs(m - 45))
    else:
        print(23, 60 - abs(m - 45))
else:
    if h > 0:
        print(h - 1, 0)
    else:
        print(23, 0)
