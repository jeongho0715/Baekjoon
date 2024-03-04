n = int(input())
num = ""

for i in range(1, n+1, 1):
    a, b = map(int, input().split())
    num += str(a+b)+"\n"

print(num)