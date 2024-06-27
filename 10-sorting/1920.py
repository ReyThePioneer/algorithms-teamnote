#1920 수 찾기

import sys

n = int(sys.stdin.readline())
arr_a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr_b = list(map(int, sys.stdin.readline().split()))

for b in arr_b:
    if b in arr_a:
        print(1)
    else:
        print(0)