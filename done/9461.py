# https://www.acmicpc.net/problem/9461 파도반 수열
import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

print(INPUT)

N = int(INPUT[0])

target = [int(i) for i in INPUT[1:]]
print(target)

P = [1, 1, 1]

for i in range(3, max(target)):
    P.append(P[i-2] + P[i-3])
    
print(P)

for x in target:
    print(P[x-1])