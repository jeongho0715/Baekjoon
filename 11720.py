n = int(input())
num = input()
num_sum = 0

for i in range(1, n+1, 1):
    num_sum += int(num[((i - 1) * (len(num) // n)):(i * (len(num) // n))])

print(num_sum)
