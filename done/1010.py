# https://www.acmicpc.net/problem/1010 다리 놓기
import sys
sys.stdin = open('input.txt')

import math

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    result = math.comb(b, a)
    print(result)