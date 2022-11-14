# https://www.acmicpc.net/problem/5597

import sys
sys.stdin = open('input.txt')

lst = list(range(1, 31))
for _ in range(28):
    lst.remove(int(sys.stdin.readline().strip()))

for k in lst:
    print(k)