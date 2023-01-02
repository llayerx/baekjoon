# https://www.acmicpc.net/problem/2108

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
cnt = [0] * 8001
keys = sorted(list(map(int, sys.stdin.readlines())))
print(round(sum(keys)/n))  # avg
print(keys[n//2]) # med
for num in keys:
    if num < 0:
        cnt[num*(-1) + 4000] += 1
    else:
        cnt[num] += 1
max_key = max(cnt)
bin = [i for i, x in enumerate(cnt) if x == max_key]
bin = [a if a <= 4000 else (-1)*(a-4000) for a in bin]
bin.sort()
print(bin[1] if len(bin) > 1 else bin[0])  # mode
print(max(keys) - min(keys))  # range