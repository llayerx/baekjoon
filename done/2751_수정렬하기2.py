# https://www.acmicpc.net/problem/2751

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(nums):
    print(num)