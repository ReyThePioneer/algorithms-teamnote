board = []

for _ in range(10):
  board.append(list(map(int, input().split())))

# 시작 (2,2)
x, y = 1, 1

while (True):
  # 갈 수 있는 곳(0)
  if (board[x][y] == 0):
    board[x][y] = 9
  # 먹이를 만나면 멈춤(2)
  elif (board[x][y] == 2):
    board[x][y] = 9
    break
  
  # 오른쪽과 아래가 모두 막히면 멈춤(1)
  if (board[x][y+1] == 1 and board[x+1][y] == 1) or (x==9 and y==9):
    break

  # 오른쪽으로 이동
  if (board[x][y+1] != 1):
    y += 1
  # 아래로 이동
  elif (board[x+1][y] != 1):
    x += 1

for i in range(10):
  for j in range(10):
    print(board[i][j], end=' ')
  print()