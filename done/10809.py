# https://www.acmicpc.net/problem/10809 알파벳찾기

deck = [-1] * 26
sentence = input()

for i in range(len(sentence)):
    deck_idx = ord(sentence[i]) - 97
    if deck[deck_idx] < 0:
        deck[deck_idx] = i

str_deck = [str(i) for i in deck]
print(' '.join(str_deck))