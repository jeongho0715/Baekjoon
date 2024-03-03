a, b = map(int, input().split())
num = ""

while a*b != 0:
    num += str(a+b)+"\n"
    a, b = map(int, input().split())

print(num)
