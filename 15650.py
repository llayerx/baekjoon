# https://www.acmicpc.net/problem/15650 N과 M (2)

from itertools import combinations
import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readline()

maxnum, count = map(int, INPUT.split())

nums = range(1, maxnum+1)
pairs = combinations(nums, count)
for pair in pairs:
    print(' '.join(list(map(str, pair))))