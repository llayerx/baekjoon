# https://www.acmicpc.net/problem/10814 나이순 정렬

import sys
sys.stdin = open('input.txt')

mems = {}
mems = list(map(str.strip, sys.stdin.readlines()[1:]))
mems.sort(key=lambda x: int(x.split()[0]))
print('\n'.join(mems))