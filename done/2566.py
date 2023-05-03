# https://www.acmicpc.net/problem/2566 최댓값

"""
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80
"""

import sys
sys.stdin = open('input.txt')

arr = list(map(str.strip, sys.stdin.readlines()))
map = {}

for row, line in enumerate(arr):
    nums = line.split()
    for col, val in enumerate(nums):
        map[val] = f"{row+1} {col+1}"

max_val = max(map.keys(), key=int)
print(max_val)
print(map[max_val])