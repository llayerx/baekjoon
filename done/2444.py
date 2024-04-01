# https://www.acmicpc.net/problem/2444 별찍기 - 7

i = int(input())

for j in range(1, i):
    print(" "*(i-j) + "*"*(2*j-1))

print("*"*(2*i-1))

for j in range(i-1, 0, -1):
    print(" "*(i-j) + "*"*(2*j-1))