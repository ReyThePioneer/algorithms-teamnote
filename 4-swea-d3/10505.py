#10505 소득 불균형

T = int(input())

for tc in range(T):
  N = int(input())
  income = list(map(int, input().split()))
  cnt = 0

  avg = sum(income) / len(income)

  for i in income:
    if i <= avg:
      cnt += 1

  print(f"#{tc + 1} {cnt}")