#2563 색종이

import sys

# 도화지 상태
colored = [[0 for _ in range(100)] for _ in range(100)]

# 색종이의 수
n = int(sys.stdin.readline())

# 색종이들의 위치 정보 (왼쪽 아래 점)
position = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    # 색칠하기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            colored[i][j] = 1

# 색종이가 칠해진 넓이
area = 0
for row in colored:
    area += sum(row)

print(area)