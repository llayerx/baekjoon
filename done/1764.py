# https://www.acmicpc.net/problem/1764 듣보잡
import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

N, M = map(int, INPUT[0].split())

A = set(INPUT[1:1+N])
B = set(INPUT[N+1:])
result = sorted(list(A.intersection(B)))
print(len(result))
print('\n'.join(result))