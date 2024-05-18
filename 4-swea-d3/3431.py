#3431 준환이의 운동관리

T = int(input())

for tc in range(T):
  L, U, X = map(int, input().split())
  ans = 0

  if X < L:
    ans = L - X
  elif X > U:
    ans = -1

  print(f"#{tc + 1} {ans}")