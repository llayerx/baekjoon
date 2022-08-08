# https://www.acmicpc.net/problem/1712

fix, var, price = map(int, input().split())
income = price - var
print('-1') if income <= 0 else print(fix // income + 1)
