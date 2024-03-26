# https://www.acmicpc.net/problem/25314 코딩은 체육과목 입니다
# import sys
i = int(input())

print("long "*(i//4 if i%4==0 else i//4 + 1) + "int")