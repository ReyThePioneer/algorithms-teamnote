#10570 제곱 팰린드롬 수

T = int(input())

for tc in range(T):
  a, b = map(int, input().split())
  cnt = 0

  for i in range(a, b + 1):
    if i in [1, 4, 9, 121, 484]:
      cnt += 1

  print(f"#{tc + 1} {cnt}")