h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())

for _ in range(n):
  l, d, x, y = map(int, input().split())

  # 막대 길이만큼 반복
  for i in range(l):
    if d == 0: # 가로 방향
      board[x-1][y-1+i] = 1
    else: # 세로 방향
      board[x-1+i][y-1] = 1

for i in range(h):
  for j in range(w):
    print(board[i][j], end=' ')
  print()