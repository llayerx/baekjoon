# https://www.acmicpc.net/problem/1157 단어공부

deck = dict()
sentence = input().upper()

for i, char in enumerate(sentence):
    if char in deck:
        deck[char] += 1
    else:
        deck[char] = 1

max_val = [k for k, v in deck.items() if v == max(deck.values())]
print('?') if len(max_val) > 1 else print(''.join(max_val))
