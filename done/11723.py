# https://www.acmicpc.net/problem/11723 집합
# 조건문, worst case 분석, 비트연산

import sys
sys.stdin = open('input.txt')

_ = input()
S = 0
ALL = (1 << 20) - 1

for row in sys.stdin:
    match row.split():
        case ['add', num]:
            S |= (1 << (int(num) - 1))
        case ['remove', num]:
            S &= ~(1 << (int(num) - 1))
        case ['check', num]:
            print(1 if (S & (1 << (int(num) - 1))) > 0 else 0)
        case ['toggle', num]:
            S ^= (1 << (int(num) - 1))
        case ['all']:
            S = ALL
        case ['empty']:
            S = 0