#2511 카드놀이

import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
result = [""] * 10

score_a = 0
score_b = 0
winner = ""

for i in range(10):
    if a[i] == b[i]:
        result[i] = "D"
        score_a += 1
        score_b += 1
    elif a[i] > b[i]:
        result[i] = "A"
        score_a += 3
    elif a[i] < b[i]:
        result[i] = "B"
        score_b += 3

if score_a == score_b:
    for i in range(10):
        if result[-1 - i] != "D":
            winner = result[-1 -i]
            break
        else:
            winner = "D"
elif score_a > score_b:
    winner = "A"
elif score_a < score_b:
    winner = "B"

print(score_a, score_b)
print(winner)