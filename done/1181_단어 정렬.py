# https://www.acmicpc.net/problem/1181

import sys
sys.stdin = open('input.txt')

words = sys.stdin.readlines()[1:]
words = list(set(map(str.strip, words)))
words.sort(key=lambda x: (len(x), str(x)))
print('\n'.join(words))