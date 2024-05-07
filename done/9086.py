# https://www.acmicpc.net/problem/9086 문자열
# 입력
"""3
ACDKJFOWIEGHE
O
AB""" 
# 결과
"""AE
OO
AB"""

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

for l in INPUT[1:]:
    l = l.replace('\n','')
    print(f'{l[0]}{l[-1]}')