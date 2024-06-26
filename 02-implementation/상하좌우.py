# 요구사항대로 충실히 구현하면 되는 문제
# 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 '시뮬레이션(Simulation) 유형으로도 분류됨

n = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)