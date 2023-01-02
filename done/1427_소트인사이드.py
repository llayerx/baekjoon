# https://www.acmicpc.net/problem/1427

import sys
sys.stdin = open('input.txt')

n = sorted(list(sys.stdin.readline()), reverse=True)
print(''.join(n))