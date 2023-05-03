# https://www.acmicpc.net/problem/2441 별 찍기 - 4

import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = " " * (i) + "*"*(n-i)
    print(line)

