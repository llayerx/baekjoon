# https://www.acmicpc.net/problem/2805 나무 자르기
# 이진탐색

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
T = list(map(int, input().split()))

l, h = 0, max(T)
cut = 0

while l <= h:
    m = (l + h) // 2
    total = sum(t - m for t in T if t > m)

    if total >= M:
        cut = m
        l = m + 1
    else:
        h = m - 1

print(cut)
