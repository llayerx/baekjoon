# https://www.acmicpc.net/problem/25304 영수증

import sys
sys.stdin = open('input.txt')

recipt = int(input())
num = int(input())

mul = lambda x: x[0] * x[1]
stuff = [mul(list(map(int, sys.stdin.readline().rstrip().split(' ')))) for _ in range(num)]

print('YES' if sum(stuff) == recipt else 'NO')