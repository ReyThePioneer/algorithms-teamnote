#12221 구구단2

T = int(input())

for tc in range(T):
  A, B = map(int, input().split())
  ans = 0

  if (A > 9) or (B > 9):
    ans = -1
  else:
    ans = A * B

  print(f"#{tc + 1} {ans}")