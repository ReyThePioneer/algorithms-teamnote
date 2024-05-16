#1970 쉬운 거스름돈

T = int(input())

for tc in range(T):
  N = int(input())
  money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

  print(f"#{tc + 1}")

  for i in money:
    print(f"{N // i}", end=' ')
    N %= i
  print()