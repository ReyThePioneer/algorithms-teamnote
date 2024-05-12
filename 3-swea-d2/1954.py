#1954 달팽이 숫자

T = int(input())

for t in range(T):
  N = int(input())
  arr = [[0] * N for _ in range(N)]
  
  for n in range(N):
    for m in range(N):
      arr[n][m] += 1

  print(f"#{t + 1}")
  print(arr)