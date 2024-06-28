#1974 스도쿠 검증

T = int(input())

for tc in range(T):
  arr = [list(map(int, input().split())) for _ in range(9)]
  ans = 1
  row = []
  col = []
  box = []
  pat = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  # row
  for y in range(9):
    row.append(arr[y])
    tmp = []
    for x in range(9):
      tmp.append(arr[x][y])
    col.append(tmp)
  
  # box
  for x in range(0, 9, 3):
    tmp = []
    for y in range(9):
      tmp += arr[y][x:x+3]
      if y % 3 == 2:
        box.append(tmp)
        tmp = []
  
  for y in range(9):
    if sorted(row[y]) != pat or sorted(col[y]) != pat or sorted(box[y]) != pat:
      ans = 0
      break

  print(f"#{tc + 1} {ans}")