# https://www.acmicpc.net/problem/1436 영화감독 숌
# import sys
# INPUT = sys.stdin.readline()
i = int(input())

count = 0
num = 1

while True:
    if "666" in str(num):
        count += 1
        if count == i:
            print(num)
            break
    num += 1
