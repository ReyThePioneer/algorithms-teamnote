#1954 달팽이 숫자

T = int(input())

for t in range(T):
  N = int(input())
  arr = [[0] * N for _ in range(N)]
  
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  def snail(x, y, d, num):
    arr[x][y] = num
    nx = x + dx[d]
    ny = y + dy[d]
    
    if num == N * N:
      return
    if (nx < 0) or (ny < 0) or (nx >= N) or (ny >= N) or (arr[nx][ny] != 0):
      d = (d + 1) % 4
      snail(x, y, d, num)
    else:
      snail(nx, ny, d, num + 1)

  snail(0, 0, 0, 1)
  print(f"#{t + 1}")
  for i in range(N):
    for j in range(N):
      print(arr[i][j], end=' ')
    print()