# https://www.acmicpc.net/problem/10816 숫자 카드 2

"""10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10""" # 3 0 0 1 2 0 0 2

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.readlines()

HAVE = list(map(int, INPUT[1].split()))
GIVEN = list(map(int, INPUT[3].split()))

# 기존 리스트를 사용해 COUNT 딕셔너리 생성
COUNT = {}
for e in HAVE:
    if e in COUNT:
        COUNT[e] += 1
    else:
        COUNT[e] = 1

# 주어진 원소의 개수를 result 리스트에 추가
result = [COUNT.get(e, 0) for e in GIVEN]

print(" ".join(map(str, result)))


# ---- GPT 개선 코드 ---- #
from collections import Counter

# HAVE 리스트의 원소 개수를 셉니다.
COUNT = Counter(HAVE)

# GIVEN 리스트의 원소에 대해 COUNT에서 개수를 조회합니다.
# Counter 객체는 없는 키에 대해 0을 반환하므로 따로 예외 처리가 필요 없습니다.
result = [COUNT[e] for e in GIVEN]

print(" ".join(map(str, result)))
