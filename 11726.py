# https://www.acmicpc.net/problem/11726 2×n 타일링

def fill2(n):
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input())
print(fill2(n) % 10007)
