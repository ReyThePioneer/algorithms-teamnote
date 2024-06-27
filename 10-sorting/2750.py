#2750 수 정렬하기

import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

for a in arr:
    print(a)