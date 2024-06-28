#5355 화성 수학

import sys

n = int(sys.stdin.readline())
exps = []

for _ in range(n):
    exps.append(sys.stdin.readline().split())

for exp in exps:
    result = float(exp[0])

    for i in range(1, len(exp)):
        if exp[i] == "@":
            result *= 3
        elif exp[i] == "%":
            result += 5
        elif exp[i] == "#":
            result -= 7

    print("{:.2f}".format(result))