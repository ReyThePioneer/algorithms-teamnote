#10817 세 수

import sys

a, b, c = map(int, sys.stdin.readline().split())

arr = []
arr.append(a)
arr.append(b)
arr.append(c)

arr.sort()

print(arr[1])