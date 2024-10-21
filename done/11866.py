# https://www.acmicpc.net/problem/11866 요세푸스 문제 0

import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

N, K = map(int, INPUT[0].split())
print(N, K)

from collections import deque

circle = deque(range(1, N+1))
result = []
while circle:
    circle.rotate(-(K-1))
    result.append(circle.popleft())  

print(f'<{", ".join(map(str, result))}>')


# ---- 백준: wjo8703 코드 참조 --------- #
# 로테이트는 K-1 만큼 작업을 하기 때문에, O(K*N)이 될 수 있음.
# 차라리 리스트에서 제거하는게 빠름

# def josephus_permutation(N, K):
#     people = list(range(1, N + 1))  # 1부터 N까지의 사람들을 리스트에 저장
#     result = []  # 제거된 순서를 저장할 리스트
#     index = 0  # 시작 인덱스

#     while people:  # 리스트가 비어있지 않은 동안 반복
#         index = (index + K - 1) % len(people)  # K번째 사람의 인덱스 계산
#         result.append(people.pop(index))  # K번째 사람 제거하고 결과에 추가

#     return result

# # 입력 받기
# N, K = map(int, input().split())
# # 요세푸스 순열 구하기
# josephus_sequence = josephus_permutation(N, K)
# # 결과 출력
# print("<" + ", ".join(map(str, josephus_sequence)) + ">") 
