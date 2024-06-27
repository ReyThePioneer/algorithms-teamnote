#10989 수 정렬하기 3

import sys

MAX_VALUE = 10001
count = [0] * MAX_VALUE

n = int(sys.stdin.readline().strip())

for _ in range(n):
    number = int(sys.stdin.readline().strip())
    count[number] += 1

for i in range(MAX_VALUE):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)