T = int(input())

for i in range(T):
  P, Q, R, S, W = map(int, input().split())
  ans = 0
  A = 0
  B = 0

  A = W * P

  if (W <= R):
    B = Q
  else:
    B = Q + (W - R) * S

  ans = min(A, B)

  print(f"#{i + 1} {ans}")

