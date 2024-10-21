# https://www.acmicpc.net/problem/10813 공바꾸기

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

N, M = map(int, INPUT[0].split())

box = [i for i in range(1, N+1)]
print(box)

for row in INPUT[1:]:
    a, b = map(int, row.split()) 
    box[a-1], box[b-1] = box[b-1], box[a-1]

final = ' '.join(map(str, box))
print(final)