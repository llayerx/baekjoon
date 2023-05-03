# https://www.acmicpc.net/problem/25305 커트라인

import sys
sys.stdin = open('input.txt')

_, cut = sys.stdin.readline().split()
lst = list(map(int, sys.stdin.readline().split()))
lst.sort(reverse=True)
print(lst[int(cut)-1])