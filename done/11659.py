# https://www.acmicpc.net/problem/11659 구간 합 구하기 4
# DP문제

import sys
sys.stdin = open('input.txt')

IN = sys.stdin.read()
data = IN.splitlines()

N, M = map(int, data[0].split())
NUMS = list(map(int, data[1].split()))

DP = [NUMS[0]]

for i in range(1, N):
    DP.append(DP[-1]+NUMS[i])

for k in range(2, M+2):
    i, j = map(int, data[k].split())
    print(DP[j-1] if i == 1 else DP[j-1] - DP[i-2])
