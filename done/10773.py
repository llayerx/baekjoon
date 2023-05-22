# https://www.acmicpc.net/problem/10773 제로

import sys
INPUT = sys.stdin.readlines()
nums = map(int, INPUT[1:])
ans = []
for n in nums:
    if n:
        ans.append(n)
    else:
        ans.pop()
print(sum(ans))