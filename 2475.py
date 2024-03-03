n = list(input().split())
serial = 0

for i in n:
    serial += int(i) ** 2
print(serial % 10)
