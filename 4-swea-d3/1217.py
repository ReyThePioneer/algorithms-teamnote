#1217 거듭 제곱

for tc in range(10):
  _ = int(input())
  n, m = map(int, input().split())
  
  ans = n ** m

  print(f"#{tc + 1} {ans}")