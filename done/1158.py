# https://www.acmicpc.net/problem/1158 요세푸스 문제

"""7 3"""

from collections import deque
import sys
sys.stdin = open('input.txt')
N, K = map(int, sys.stdin.readline().split())

circle = deque(range(1, N+1))
result = []
while circle:
    circle.rotate(-K+1)
    result.append(circle.popleft())

print(f'<{", ".join(map(str, result))}>')