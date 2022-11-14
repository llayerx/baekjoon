# https://www.acmicpc.net/problem/10870

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
fibo = [0, 1] + [0 for _ in range(n-1)]
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo)
print(fibo[n])
