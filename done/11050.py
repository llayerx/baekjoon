# https://www.acmicpc.net/problem/11050 이항 계수 1
from math import factorial
import sys
sys.stdin = open('input.txt')
INPUT = sys.stdin.read().splitlines()

N, K = map(int, INPUT[0].split())
print(N, K)

print(int(factorial(N)/(factorial(K)*factorial(N-K))))

# GPT 
# 함수가 있다.

# import math

# def binomial_coefficient(n, k):
#     return math.comb(n, k)

# # 예시 사용
# n = 5
# k = 2
# result = binomial_coefficient(n, k)
# print(f"이항계수 C({n}, {k})는 {result}입니다.")
