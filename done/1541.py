# https://www.acmicpc.net/problem/1541 잃어버린 괄호
# 기호 처리?

import sys
sys.stdin = open('input.txt')

IN = input()

if '-' in IN:
    q = IN.split('-')
    a = sum(map(int, q[0].split('+')))

    for num in q[1:]:
        a -= sum(map(int, num.split('+')))
        
    print(a)
else:
    IN = IN.split('+')
    print(sum(map(int, IN)))
    