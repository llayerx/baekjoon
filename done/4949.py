# https://www.acmicpc.net/problem/4949 균형잡힌 세상
# 데이터 입력과 나누기 방법. 문제를 잘 읽어보자... 마지막줄 예외처리.

import sys
sys.stdin = open('input.txt')

def clean(s):
    return ''.join([c for c in s if c in "()[]"])

data = sys.stdin.read().splitlines()

for row in data[:-1]:
    q = []
    try:
        for c in clean(row):
            if c in "([":
                q.append(c)
            else:
                if q.pop()+c not in ["()", "[]"]:
                    raise ValueError
        if len(q) == 0:
            print("yes")
        else:
            raise ValueError
    except:
        print("no")