# https://www.acmicpc.net/problem/5622

dial = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
string = input().lower()
sum = 0
for char in string:
    for i, key in enumerate(dial):
        if char in key:
            sum += i + 3
print(sum)

