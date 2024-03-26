# https://www.acmicpc.net/problem/2164 카드2


# i = int(input())

# if i < 3:
#     print(i)
# else:
#     x = 0
#     while 2 ** x < i:
#         x += 1
#     print(int(2 * (i - 2 ** (x-1))))

# GPT 제안 코드
i = int(input())
# 주어진 수열의 길이가 2의 거듭제곱인지 확인
if i & (i - 1) == 0:
    print(i)
else:
    # 가장 큰 2의 거듭제곱 찾기
    m = 1
    while m <= n:
        m *= 2
    m //= 2
    # 남은 수열의 길이 구하기
    remain = n - m
    # 남은 수열의 첫 번째 수 구하기
    print(2*remain)

