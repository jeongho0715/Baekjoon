h, m = map(int, input().split())

if h > 0:
    print(h-1, 60-abs(m-45))
else:
    print(23, 60-abs(m-45))
