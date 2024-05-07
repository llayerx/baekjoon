# https://www.acmicpc.net/problem/1932 정수 삼각형

"""5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5"""

import sys
sys.stdin = open('input.txt')

data = sys.stdin.readlines()
MAX = int(data[0])  # 첫 번째 줄에서 MAX 값을 읽음
MAP = []

for idx in range(1, MAX + 1):  # MAX만큼 읽어서 지도로 저장
    line = list(map(int, data[idx].split()))  
    MAP.append(line)

for i in range(MAX-2, -1, -1):  # 바닥부터 합치며 올라옴
    for idx, j in enumerate(MAP[i]):
        MAP[i][idx] += max(MAP[i+1][idx], MAP[i+1][idx+1])  # 더 큰값 더하기
print(MAP[0][0])