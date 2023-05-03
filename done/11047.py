# https://www.acmicpc.net/problem/11047 동전 0
import sys
sys.stdin = open('input.txt') 

all = sys.stdin.readlines()
_, sum = map(int, all[0][:-1].split(' '))
coins = list(map(int, all[1:]))[::-1]

count = 0 
for coin in coins:
    n, l = divmod(sum, coin)
    count += n
    sum = l
print(count)
