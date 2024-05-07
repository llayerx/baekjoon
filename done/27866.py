# https://www.acmicpc.net/problem/27866 문자와 문자열

import sys
sys.stdin = open('input.txt')

WORD = sys.stdin.readline()
IDX = int(sys.stdin.readline())
print(WORD[IDX-1])


