# https://www.acmicpc.net/problem/9095 1,2,3 더하기

import sys

sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

numbers = list(map(int, INPUT[1:]))

dp = [0] * (max(numbers)+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max(numbers)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in numbers:
    print(dp[num])
    

    