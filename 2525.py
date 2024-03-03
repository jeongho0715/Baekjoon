h, m = map(int, input().split())
t = int(input())

if m+t >= 60:
    if h+((m+t)//60) >= 24:
        h = abs(24-(h+((m+t)//60)))
    else:
        h = h+((m+t)//60)
m = (m+t)%60
print(h, m)
