# https://www.acmicpc.net/problem/11653

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
k = 2

while n >= k:
    if divmod(n, k)[1] == 0:
        print(k)
        n /= k
    else:
        k += 1
