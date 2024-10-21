# https://www.acmicpc.net/problem/10810 공 넣기
import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

N, M = map(int, INPUT[0].split())

BASKET = [0 for _ in range(N)]
print(BASKET)

for row in INPUT[1:]:
    i, j, k = map(int, row.strip().split())    
    BASKET[i-1:j] = [k] * (j - i + 1) 
    
print(' '.join(map(str, BASKET)))
