# https://www.acmicpc.net/problem/2675

loop = int(input())

for i in range(loop):
    mul, sentence = map(str, input().split())
    out = ''
    for char in sentence:
        out += f'{char*int(mul)}'
    print(out)