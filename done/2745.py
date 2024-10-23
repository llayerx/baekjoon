# https://www.acmicpc.net/problem/2745 진법 변환

import sys
sys.stdin = open('input.txt')

CONV = {**{str(i): i for i in range(0, 10)}, **{chr(i): i - 55 for i in range(65, 91)}}

def ToN(t, n):
    r = 0
    length = len(t)
    
    for i in range(length):
        a = CONV[t[length - 1 - i]]
        r += a * (n ** i)
    
    return r

T, N = input().split()

print(ToN(T, int(N)))