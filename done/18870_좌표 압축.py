# https://www.acmicpc.net/problem/18870

import sys
sys.stdin = open('input.txt')

lst = list(map(int, sys.stdin.readlines()[1].split()))
hash = {}
cnt = 0
for num in sorted(lst):
    if num not in hash:
        hash[num] = cnt
        cnt += 1
r_lst = [hash[x] for x in lst]
print(' '.join(map(str, r_lst)))
