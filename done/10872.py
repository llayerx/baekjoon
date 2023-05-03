# https://www.acmicpc.net/problem/10872 팩토리얼

n = int(input())
rst = 1
while n > 0:
    rst *= n
    n -= 1
print(rst)
