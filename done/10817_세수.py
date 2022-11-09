# https://www.acmicpc.net/problem/10817
# 세 수 중 두번째 큰수

lst = map(int, input().split())
print(sorted(lst)[1])