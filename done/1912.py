# https://www.acmicpc.net/problem/1912 연속합

"""10
2 1 -4 3 4 -4 6 5 -5 1"""

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

DP = list(map(int, INPUT[1].split()))

for idx in range(len(DP)-2, -1, -1):
    DP[idx] = max(DP[idx], DP[idx] + DP[idx+1])
        
print(max(DP))