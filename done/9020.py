# https://www.acmicpc.net/problem/9020 골드바흐의 추측

import sys
sys.stdin = open('input.txt')

orders = list(map(int, sys.stdin.readlines()))[1:]
limit = 10000

a = [False,False] + [True]*(limit-1)
primes={}
for i in range(2, limit+1):
    if a[i]:
        primes[i] = True
        for j in range(2*i, limit+1, i):
            a[j] = False
    else:
        primes[i] = False

for n in orders:
    half = n // 2
    while half:
        if primes[half] and primes[n - half]:
            print(half, n-half)
            break
        half -= 1