#2001 파리 퇴치

T = int(input())

for tc in range(T):
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
  max_sum = 0

  for i in range(N - (M - 1)):
    for j in range(N - (M - 1)):
      temp = 0
      for l in range(i, i + M):
        for o in range(j, j + M):
          temp += arr[l][o]
  
      if temp > max_sum:
        max_sum = temp
        
  print(f"#{tc + 1} {max_sum}")