# https://www.acmicpc.net/problem/1316 그룹단어체커

from itertools import groupby

a = int(input())

check = 0
while a:
    a -= 1
    check += 1
    string = input()
    trim = ''.join(c for c, _ in groupby(string))

    for char in trim:
        if trim.count(char) > 1:
            check -= 1
            break
print(check)




