# https://www.acmicpc.net/problem/2579 계단 오르기

import sys
INPUT = sys.stdin.readlines()
print(INPUT)

stairs = [int(x) for x in INPUT[1:]]
n = len(stairs)
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    dp = [0] * 4
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, len(stairs)):
        dp[3] = max(dp[1] + stairs[i], dp[0] + stairs[i-1] + stairs[i])
        print(f'STEP {i}: DP {dp}')
        dp.pop(0)
        dp.append(0)
    print(dp[-2])