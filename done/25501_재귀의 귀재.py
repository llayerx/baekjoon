# https://www.acmicpc.net/problem/25501

def recursion(s, l, r):
    if l >= r:
        print(f'1 {l+1}')
        return 1
    elif s[l] != s[r]:
        print(f'0 {l+1}')
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().strip()
    isPalindrome(word)

