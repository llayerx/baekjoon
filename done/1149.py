# https://www.acmicpc.net/problem/1149 RGB거리

INPUT = """6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91""".split("\n")

import sys
# INPUT = sys.stdin.readlines()

price = [[int(x) for x in y.split(' ')] for y in INPUT[1:]]
print(price)

n = len(price)
dp = [price[0], [0] * 3]
for i in range(1, n):
    dp[1][0] = price[i][0] + min(dp[0][1], dp[0][2])
    dp[1][1] = price[i][1] + min(dp[0][0], dp[0][2])
    dp[1][2] = price[i][2] + min(dp[0][0], dp[0][1])

    dp[0] = dp[1][:]

result = min(dp[-1])
print(result)
