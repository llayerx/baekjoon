# https://www.acmicpc.net/problem/10989 수 정렬하기 3

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
lst = {}

for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] = lst.get(num, 0) + 1

for i in range(10001):
    if i not in lst:
        continue
    while lst[i]>2000:  #조금 빠르게
        print(f'{i}\n'*2000,end='')
        lst[i]-=2000
    print(f'{i}\n'*lst[i],end='')
    