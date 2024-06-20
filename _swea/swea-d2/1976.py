#1976 시각 덧셈

T = int(input())

for tc in range(T):
  h1, m1, h2, m2 = list(map(int, input().split()))
  
  hour = h1 + h2
  if hour > 12:
    hour -= 12
  
  min = m1 + m2
  if min > 59:
    min -= 60
    hour += 1

  print(f"#{tc + 1} {hour} {min}")