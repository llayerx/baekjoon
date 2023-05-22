# https://www.acmicpc.net/problem/1018 체스판 다시 칠하기

wb = """WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW""".split("\n")

import sys
INPUT = sys.stdin.readlines()
h, w = map(int, INPUT[0].split(' '))
MAP = INPUT[1:]
# MAP = [[1 if x == 'B' else 0 for x in y] for y in INPUT[1:]]

def diff(slice, board):
    count = 0
    print(slice, board)
    for i in range(8):
        line_a = slice[i]
        line_b = board[i]
        
        for chr1, chr2 in zip(line_a, line_b):
            if chr1 != chr2:
                count += 1
            
    return count

best = float("inf")
for y in range(h-7):
    for x in range(w-7):
        sliced_MAP = [row[x:x+8] for row in MAP[y:y+8]]
        cnt = min(diff(sliced_MAP, wb), diff(sliced_MAP, wb[::-1]))
        best = min(best, cnt)
print(best)

