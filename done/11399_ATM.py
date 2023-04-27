# https://www.acmicpc.net/problem/11399
from itertools import accumulate
import sys
sys.stdin = open('input.txt')

sys.stdin.readline()  # 첫줄 버림 필요없음.

n = list(map(int, sys.stdin.readline().split(' ')))
ans = accumulate(sorted(n))
print(sum(ans))
