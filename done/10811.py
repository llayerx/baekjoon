# https://www.acmicpc.net/problem/10811 바구니 뒤집기

import sys
sys.stdin = open('input.txt')

IN = sys.stdin.read().splitlines()

N, M = map(int, IN[0].split())
ORDER = [i for i in range(N+1)]

for row in IN[1:]:
    i, j = map(int, row.split())
    while i < j:
        ORDER[i], ORDER[j] = ORDER[j], ORDER[i]
        i+=1
        j-=1
print(" ".join(map(str, ORDER[1:])))