# https://www.acmicpc.net/problem/2941 크로아티아알파벳

deck = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

numchar = len(string)
for char in deck:
    dup = string.count(char)
    if dup > 0:
        numchar -= string.count(char)

print(numchar)