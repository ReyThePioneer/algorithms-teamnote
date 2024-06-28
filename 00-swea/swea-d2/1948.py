import datetime as datetime

T = int(input())

for t in range(T):
  m1, d1, m2, d2 = map(int, input().split())
  ans = 0

  dt1 = datetime.date(2023, m1, d1)
  dt2 = datetime.date(2023, m2, d2)
  ans = (dt2 - dt1).days + 1

  print(f"#{t + 1} {ans}")