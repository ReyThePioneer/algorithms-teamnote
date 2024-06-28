#2902 KMP는 왜 KMP일까?

import sys

names = list(sys.stdin.readline().split('-'))

for name in names:
    print(name[0], end="")